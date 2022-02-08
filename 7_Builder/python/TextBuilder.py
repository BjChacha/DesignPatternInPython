from tokenize import String
from Builder import Builder

class TextBuilder(Builder):

    def __init__(self) -> None:
        self._buffer = ""

    def make_title(self, title):
        self._buffer += "========================\n"
        self._buffer += f"[{title}] \n"
        self._buffer += "\n"

    def make_string(self, string):
        self._buffer += f"■ {string}\n"
        self._buffer += "\n"

    def make_items(self, items):
        for item in items:
            self._buffer += f"  ·{item}\n"
        self._buffer += "\n"

    def close(self):
        self._buffer += "========================\n"

    def get_result(self) -> String:
        return self._buffer