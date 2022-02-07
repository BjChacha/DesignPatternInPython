class Banner:
    def __init__(self, string):
        self._string = string

    def show_with_paren(self):
        print(f'({self._string})')

    def show_with_aster(self):
        print(f'*{self._string}*')