from sb_foo_client.main import FooClient


class FooIndexer:
    def __init__(self, foo):
        self.foo = foo
        self.client = FooClient(foo=foo)
        print(self.client.things())

    def do(self):
        pass

    def stuff(self):
        pass

    def things(self):
        pass
