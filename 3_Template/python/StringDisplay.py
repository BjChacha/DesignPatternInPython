from AbstractDisplay import AbstractDisplay

class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.string = string
        self.width = len(string.encode('gbk'))

    def open(self):
        self.print_line()

    def print(self):
        print(f"|{self.string}|")
    
    def close(self):
        self.print_line()
    
    def print_line(self):
        print("+" + "-" * self.width + "+")