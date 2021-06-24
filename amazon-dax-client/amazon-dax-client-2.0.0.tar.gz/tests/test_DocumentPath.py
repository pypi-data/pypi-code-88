from amazondax.DocumentPath import DocumentPath

import pytest

TEST_PATHS = [
    ('a.b.c.d[0].e.f[1]', ['a', 'b', 'c', 'd', 0, 'e', 'f', 1]),
    ('a.b[1][0][2].c.d[0].e.f[1]', ['a', 'b', 1, 0, 2, 'c', 'd', 0, 'e', 'f', 1]),
    (('#a.b[1][0][2].c.d[0].e.#f[1]', {'#a': 'a.a.a', '#f': 'f.f.f'}), ['a.a.a', 'b', 1, 0, 2, 'c', 'd', 0, 'e', 'f.f.f', 1]),
]

@pytest.mark.parametrize("path,expected", TEST_PATHS)
def test_document_path(path, expected):
    if isinstance(path, tuple):
        path, attr_names = path
    else:
        attr_names = None

    actual = DocumentPath.from_path(path, attr_names)
    assert actual.elements == expected

