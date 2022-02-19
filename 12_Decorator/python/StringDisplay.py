from asyncio.windows_events import NULL
from Display import Display

class StringDisplay(Display):

    def __init__(self, string):
        self._string = string

    def get_columns(self):
        return len(self._string.encode("gbk"))

    def get_rows(self):
        return 1

    def get_row_text(self, row):
        return self._string if row == 0 else NULL