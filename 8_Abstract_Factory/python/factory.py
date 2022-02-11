import importlib

class Factory:

    @staticmethod
    def get_factory(modulename, classname):
        try:
            module = importlib.import_module(modulename)
            aclass = getattr(module, classname)
            factory = aclass()
            return factory
        except AttributeError as e:
            print(e)
        

    def create_link(self, caption, url):
        raise NotImplementedError

    def create_tray(self, caption):
        raise NotImplementedError

    def create_page(self, title, author):
        raise NotImplementedError


class Item:

    def __init__(self, caption):
        self._caption = caption

    def make_HTML(self):
        raise NotImplementedError


class Link(Item):

    def __init__(self, caption, link):
        super().__init__(caption)
        self._link = link


class Tray(Item):

    def __init__(self, caption):
        super().__init__(caption)
        self._tray = []

    def add(self, item):
        self._tray.append(item)


class Page:

    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._content = []

    def add(self, item):
        self._content.append(item)

    def output(self):
        try:
            with open(f"{self._title}.html", 'w', encoding='utf8') as f:
                f.write(self.make_HTML())
        except IOError as e:
            print(e)

    def make_HTML(self):
        raise NotImplementedError
