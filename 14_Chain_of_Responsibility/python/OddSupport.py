from Support import Support

class OddSupport(Support):

    def resolve(self, trouble):
        return trouble.get_number() % 2 == 1