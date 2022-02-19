from dis import dis
from Border import Border

class SideBorder(Border):

    def __init__(self, display, ch):
        super().__init__(display)
        self._border_char = ch

    def get_columns(self):
        return self._display.get_columns() + 2

    def get_rows(self):
        return self._display.get_rows()

    def get_row_text(self, row):
        return f"{self._border_char}{self._display.get_row_text(row)}{self._border_char}"