from DisplayImpl import DisplayImpl

class StringDisplayImpl(DisplayImpl):

    def __init__(self, string):
        self._string = string
        self._width = len(string.encode('utf8'))
    
    def raw_open(self):
        self.print_line()

    def raw_print(self):
        print(f"|{self._string}|")

    def raw_close(self):
        self.print_line()

    def print_line(self):
        print("+" + "-" * self._width + "+")

