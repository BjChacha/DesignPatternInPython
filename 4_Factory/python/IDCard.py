from Framework import Factory, Product

class IDCard(Product):

    def __init__(self, owner):
        print(f'制作{owner}的ID卡。')
        self.owner = owner

    def use(self):
        print(f'使用{self.owner}的ID卡。')

    def get_owner(self):
        return self.owner;


class IDCardFactory(Factory):

    def __init__(self):
        self.owners = []

    def _createProduct(self, owner):
        return IDCard(owner)

    def _registerProduct(self, product):
        self.owners.append(product.get_owner())

    def get_owners(self):
        return self.owners