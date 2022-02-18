from Entry import Entry

class Directory(Entry):

    def __init__(self, name):
        self._name = name
        self._directory = []

    def get_name(self):
        return self._name

    def get_size(self):
        return sum([entry.get_size() for entry in self._directory])

    def add(self, entry):
        self._directory.append(entry)
        return self

    def print_list(self, prefix=""):
        print(f"{prefix}/{self}")
        for entry in self._directory:
            entry.print_list(f"{prefix}/{self._name}")
