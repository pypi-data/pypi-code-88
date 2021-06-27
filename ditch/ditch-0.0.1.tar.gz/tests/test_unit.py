from ditch import foo_maker


def test_foo_maker():
    assert foo_maker() == 'foo'