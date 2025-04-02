import re
from itertools import count
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template, Undefined
from markdown2 import markdown
from markupsafe import Markup

ROOT_DIR = Path(__file__).parents[2]
ATTACK_DATA_DIR = ROOT_DIR / "data" / "attack" / "stix-2.0"
PUBLIC_DIR = ROOT_DIR / "public"
TEMPLATE_DIR = ROOT_DIR / "templates"
CITATION_TEXT = "(Citation: "
CITATION_LEN = len(CITATION_TEXT)


def attack_markdown_filter(text, references=None):
    # Some objects don't have a description, and jinja will pass us a special
    # "Undefined" object. In that case we return an empty string.
    if isinstance(text, Undefined):
        return ""

    # If we have references, then replace the citation texts with superscripts
    # and append a list of references after the text.
    if references:
        footnote_counter = count(1)
        footnote_nums = dict()
        references = {
            r["source_name"]: (r["description"], r.get("url"))
            for r in references
            if "description" in r and "url" in r
        }

        # Replace citations with footnote links. Citations are contained in
        # parentheses but the citation itself may also contain parentheses, so
        # we can't just use a regex to find them. We have to count balanced
        # parentheses.
        new_text = ""
        next_citation_idx = 0
        end_idx = 0
        while next_citation_idx < len(text):
            # Extract a source name
            last_citation_idx = next_citation_idx
            next_citation_idx = text.find(CITATION_TEXT, next_citation_idx)
            if next_citation_idx == -1:
                break
            start_idx = next_citation_idx + CITATION_LEN
            end_idx = start_idx
            paren_count = 1
            while paren_count > 0:
                if text[end_idx] == "(":
                    paren_count += 1
                elif text[end_idx] == ")":
                    paren_count -= 1
                end_idx += 1
            citation_name = text[start_idx : end_idx - 1]

            # Add all the text up to the citation:
            new_text += text[last_citation_idx:next_citation_idx]

            # Replace the citation text with a citation superscript. In rare cases, the text
            # refers to a non-existent citation, and we just skip those.
            if citation_name in references:
                reference = references[citation_name]
                if citation_name not in footnote_nums:
                    footnote_nums[citation_name] = next(footnote_counter)
                new_text += (
                    f"<sup>[[{footnote_nums[citation_name]}]]({reference[1]})</sup>"
                )

            next_citation_idx = end_idx

        # Add all text from the last citation to the end of the string. (If there are
        # no citations, this adds the whole string.)
        new_text += text[end_idx:]

        # List all the citations beneath the main text.
        if end_idx > 0:
            new_text += "\n\n**References:**\n\n"
            num_footnotes = {v: k for k, v in footnote_nums.items()}
            for num, ref_key in num_footnotes.items():
                reference = references[ref_key]
                new_text += f"{num}. [{reference[0]}]({reference[1]})\n"

        text = new_text

    rendered_text = markdown(text)
    return Markup(rendered_text)


_environment = Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=True)
_environment.filters["attack_markdown"] = attack_markdown_filter


def load_template(name: str) -> Template:
    """
    Load a jinja2 template by name from the templates directory.

    Args:
        name: e.g. "nav.html"
    """
    return _environment.get_template(name)
