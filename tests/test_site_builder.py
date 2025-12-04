from attack_sync.site_builder import get_version_pairs


def test_version_pairs():
    versions = [
        (14, 0),
        (14, 1),
        (15, 0),
        (15, 1),
        (15, 2),
        (16, 0),
        (16, 1),
    ]
    expected_pairs = {
        (14, 0): [(14, 1), (15, 0), (15, 1), (15, 2), (16, 0), (16, 1)],
        (14, 1): [(15, 0), (15, 1), (15, 2), (16, 0), (16, 1)],
        (15, 0): [(15, 1), (15, 2), (16, 0), (16, 1)],
        (15, 1): [(15, 2), (16, 0), (16, 1)],
        (15, 2): [(16, 0), (16, 1)],
        (16, 0): [(16, 1)],
        (16, 1): []
    }
    assert expected_pairs == get_version_pairs(versions)
