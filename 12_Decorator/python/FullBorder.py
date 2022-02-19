from Border import Border

class FullBorder(Border):
    
    def get_columns(self):
        return self._display.get_columns() + 2

    def get_rows(self):
        return self._display.get_rows() + 2

    def get_row_text(self, row):
        if row == 0 or row == self._display.get_rows() + 1:
            return f"+{self._make_line('-', self._display.get_columns())}+"
        else:
            return f"|{self._display.get_row_text(row-1)}|"

    def _make_line(self, ch, count):
        return ch * count
