class Trouble:

    def __init__(self, number):
        self._number = number

    def get_number(self):
        return self._number

    def __str__(self):
        return f'[Trouble {self._number}]'