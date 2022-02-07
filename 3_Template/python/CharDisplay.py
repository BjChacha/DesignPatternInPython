from AbstractDisplay import AbstractDisplay

class CharDisplay(AbstractDisplay):

    def __init__(self, char):
        self.char = char

    def _open(self):
        print("<<")

    def _print(self):
        print(self.char)

    def _close(self):
        print(">>")