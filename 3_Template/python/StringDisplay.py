from AbstractDisplay import AbstractDisplay

class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.string = string
        self.width = len(string.encode('gbk'))

    def _open(self):
        self._print_line()

    def _print(self):
        print(f"|{self.string}|")
    
    def _close(self):
        self._print_line()
    
    def _print_line(self):
        print("+" + "-" * self.width + "+")