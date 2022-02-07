from Framework import Product

class MessageBox(Product):
    
    def __init__(self, decochar):
        self._decochar = decochar
    
    def use(self, string):
        length = len(string.encode('gbk'))
        print(self._decochar * (length + 4))
        print(f'{self._decochar} {string} {self._decochar}')
        print(self._decochar * (length + 4))

    def create_clone(self):
        return self._clone(self)