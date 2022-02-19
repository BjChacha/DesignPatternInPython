class Display:

    def get_columns(self):
        raise NotImplementedError

    def get_rows(self):
        raise NotImplementedError

    def get_row_text(self, row):
        raise NotImplementedError

    def show(self):
        rows = self.get_rows()
        for i in range(rows):
            print(self.get_row_text(i))