from sb_client_core import ClientCore


class FooClient(ClientCore):
    """FOOO 6"""
    def __init__(self, foo):
        super().__init__(foo=foo)
        self.foo = foo

    def do(self):
        pass

    def things(self):
        pass

    def stuff(self):
        pass
