from Support import Support

class LimitSupport(Support):

    def __init__(self, name, limit):
        self._limit = limit
        super().__init__(name)

    def resolve(self, trouble):
        return trouble.get_number() < self._limit