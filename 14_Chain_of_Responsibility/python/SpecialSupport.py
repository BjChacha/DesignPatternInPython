from unicodedata import numeric
from Support import Support

class SpecialSupport(Support):

    def __init__(self, name, number):
        self._number = number
        super().__init__(name)

    def resolve(self, trouble):
        return trouble.get_number() == self._number