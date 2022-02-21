from Entry import Entry

class Directory(Entry):

    def __init__(self, name):
        self._name = name
        self._dir = []

    def get_name(self):
        return self._name

    def get_size(self):
        return sum([e.get_size() for e in self._dir])

    def iterator(self):
        return self._dir.__iter__()

    def add(self, entry):
        self._dir.append(entry)
        return self

    def accept(self, visitor):
        visitor.visit(self)