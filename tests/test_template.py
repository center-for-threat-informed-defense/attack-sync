from attack_sync.template import attack_markdown_filter


def test_markdown():
    expected = "<p>hello <em>world</em> how <strong>are</strong> you?</p>\n"
    actual = attack_markdown_filter("hello *world* how **are** you?")
    assert expected == actual


def test_markdown_citations():
    references = [
        {
            "source_name": "mitre-attack",
            "url": "https://attack.mitre.org/techniques/T1003/005",
            "external_id": "T1003.005",
        },
        {
            "source_name": "foo",
            "description": "John Doe. (1970, January 1). Yada yada. Retrieved January 1, 1970.",
            "url": "https://foo.example",
        },
        {
            "source_name": "bar",
            "description": "Jane Doe. (1970, January 2). Yada yada. Retrieved January 2, 1970.",
            "url": "https://bar.example",
        },
    ]
    md = (
        "Somebody said this.(Citation: foo) Somebody said that.(Citation: bar) "
        "Somebody said this and and that.(Citation: foo)(Citation: bar)"
    )
    expected = (
        '<p>Somebody said this.<sup><a href="https://foo.example">[1]</a></sup> '
        'Somebody said that.<sup><a href="https://bar.example">[2]</a></sup> '
        'Somebody said this and and that.<sup><a href="https://foo.example">[1]</a></sup><sup><a href="https://bar.example">[2]</a></sup></p>\n\n'
        "<p><strong>References:</strong></p>\n\n"
        "<ol>\n"
        '<li><a href="https://foo.example">John Doe. (1970, January 1). Yada yada. Retrieved January 1, 1970.</a></li>\n'
        '<li><a href="https://bar.example">Jane Doe. (1970, January 2). Yada yada. Retrieved January 2, 1970.</a></li>\n'
        "</ol>\n"
    )
    actual = attack_markdown_filter(md, references)
    assert expected == actual


def test_markdown_citation_with_parens():
    """Parentheses in the citation source name is a special case we need to handle."""
    references = [
        {
            "source_name": "mitre-attack",
            "url": "https://attack.mitre.org/techniques/T1003/005",
            "external_id": "T1003.005",
        },
        {
            "source_name": "foo(bar)",
            "description": "Yada yada",
            "url": "https://foo.example",
        },
    ]
    md = "Somebody said this.(Citation: foo(bar))"
    expected = (
        '<p>Somebody said this.<sup><a href="https://foo.example">[1]</a></sup></p>\n\n'
        "<p><strong>References:</strong></p>\n\n"
        "<ol>\n"
        '<li><a href="https://foo.example">Yada yada</a></li>\n'
        "</ol>\n"
    )
    actual = attack_markdown_filter(md, references)
    assert expected == actual


def test_markdown_no_citation():
    """Markdown that has references but doesn't include any citations in the text."""
    references = [
        {
            "source_name": "mitre-attack",
            "url": "https://attack.mitre.org/techniques/T1003/005",
            "external_id": "T1003.005",
        },
        {
            "source_name": "foo(bar)",
            "description": "Yada yada",
            "url": "https://foo.example",
        },
    ]
    md = "Somebody said this."
    expected = "<p>Somebody said this.</p>\n"
    actual = attack_markdown_filter(md, references)
    assert expected == actual


def test_markdown_erroneous_citation():
    """Markdown that has references but doesn't include any citations in the text."""
    references = [
        {
            "source_name": "mitre-attack",
            "url": "https://attack.mitre.org/techniques/T1003/005",
            "external_id": "T1003.005",
        },
        {
            "source_name": "foo",
            "description": "Yada yada",
            "url": "https://foo.example",
        },
        {
            "source_name": "bar",
            "description": "Yada yada",
            "url": "https://bar.example",
        },
    ]
    md = "Somebody said this.(Citation: fob)(Citation: bar)"
    expected = (
        '<p>Somebody said this.<sup><a href="https://bar.example">[1]</a></sup></p>\n\n'
        "<p><strong>References:</strong></p>\n\n"
        "<ol>\n"
        '<li><a href="https://bar.example">Yada yada</a></li>\n'
        "</ol>\n"
    )
    actual = attack_markdown_filter(md, references)
    assert expected == actual
