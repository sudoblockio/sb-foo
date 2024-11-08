from sb_foo_client import FooClient


def test_this():
    f = FooClient(foo="bar")

    assert f
