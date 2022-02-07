from AbstractDisplay import AbstractDisplay

class CharDisplay(AbstractDisplay):

    def __init__(self, char):
        self._char = char

    def _open(self):
        print("<<")

    def _print(self):
        print(self._char)

    def _close(self):
        print(">>")