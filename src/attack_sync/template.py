import re
from itertools import count
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template
from markdown2 import markdown
from markupsafe import Markup

ROOT_DIR = Path(__file__).parents[2]
ATTACK_DATA_DIR = ROOT_DIR / "data" / "attack" / "stix-2.0"
PUBLIC_DIR = ROOT_DIR / "public"
TEMPLATE_DIR = ROOT_DIR / "templates"
CITATION_RE = re.compile(r"\(Citation: (.+?)\)")


def attack_markdown_filter(text, references=None):
    footnote_counter = count(1)
    footnote_nums = dict()

    def footnote(match_):
        ref_key = match_.group(1)
        reference = references[ref_key]
        if ref_key not in footnote_nums:
            footnote_nums[ref_key] = next(footnote_counter)
        return f"<sup>[[{footnote_nums[ref_key]}]]({reference[1]})</sup>"

    if references:
        references = {
            r["source_name"]: (r["description"], r.get("url"))
            for r in references
            if "description" in r and "url" in r
        }
        text = CITATION_RE.sub(footnote, text)
        text += "\n\n**References:**\n\n"
        num_footnotes = {v: k for k, v in footnote_nums.items()}
        for num, ref_key in num_footnotes.items():
            reference = references[ref_key]
            text += f"{num}. [{reference[0]}]({reference[1]})\n"

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
