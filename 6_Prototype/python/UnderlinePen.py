from tkinter import Frame
from Framework import Product

class UnderlinePen(Product):

    def __init__(self, ulchar):
        self._ulchar = ulchar
    
    def use(self, string):
        length = len(string.encode('gbk'))
        print(f'"{string}"')
        print(f' {self._ulchar * length} ')

    def create_clone(self):
        return self._clone(self)