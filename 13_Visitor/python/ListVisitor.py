from Visitor import Visitor
from File import File
from Directory import Directory

class ListVisitor(Visitor):

    def __init__(self):
        self._currentdir = ""

    def visit(self, entry):
        if isinstance(entry, File):
            print(f"{self._currentdir}/{entry}")
        elif isinstance(entry, Directory):
            print(f"{self._currentdir}/{entry}")
            savedir = self._currentdir
            self._currentdir += f"/{entry.get_name()}"
            for e in entry.iterator():
                e.accept(self)
            self._currentdir = savedir
