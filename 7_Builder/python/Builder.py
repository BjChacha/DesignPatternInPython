class Builder:

    def make_title(self, title):
        raise NotImplementedError

    def make_string(self, string):
        raise NotImplementedError

    def make_items(self, items):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError