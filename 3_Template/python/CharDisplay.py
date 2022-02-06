from AbstractDisplay import AbstractDisplay

class CharDisplay(AbstractDisplay):

    def __init__(self, char):
        self.char = char

    def open(self):
        print("<<")

    def print(self):
        print(self.char)

    def close(self):
        print(">>")