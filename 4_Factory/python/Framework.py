class Product:
    def use(self):
        raise NotImplementedError


class Factory:
    def create(self, owner):
        product = self._createProduct(owner)
        self._registerProduct(product)
        return product

    def _createProduct(self, owner):
        raise NotImplementedError

    def _registerProduct(self, product):
        raise NotImplementedError