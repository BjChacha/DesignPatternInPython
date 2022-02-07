import copy

class Product:
    def use(self, string):
        raise NotImplementedError

    def create_clone(self):
        raise NotImplementedError

    def _clone(self, obj):
        # try to deepcopy(self)
        return copy.deepcopy(obj)


class Manager:
    
    def __init__(self):
        self._showcase = {}
    
    def register(self, name, proto):
        self._showcase[name] = proto

    def create(self, name):
        return self._showcase[name].create_clone()
