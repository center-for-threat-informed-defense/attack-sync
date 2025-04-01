from attack_sync.template import attack_markdown_filter


def test_markdown():
    expected = "<p>hello <em>world</em> how <strong>are</strong> you?</p>\n"
    actual = attack_markdown_filter("hello *world* how **are** you?")
    assert expected == actual


def test_markdown_references():
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
        'Somebody said this and and that.<sup><a href="https://foo.example">[1]</a></sup><sup><a href="https://bar.example">[2]</a></sup>\n'
        "<strong>References:</strong>\n"
        '1. <a href="https://foo.example">John Doe. (1970, January 1). Yada yada. Retrieved January 1, 1970.</a>\n'
        '2. <a href="https://bar.example">Jane Doe. (1970, January 2). Yada yada. Retrieved January 2, 1970.</a></p>\n'
    )
    actual = attack_markdown_filter(md, references)
    assert expected == actual
