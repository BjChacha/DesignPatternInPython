from Iterator import Iterator


class BookShelfIterator(Iterator):

    def __init__(self, bookshelf):
        self.bookshelf = bookshelf
        self.last = 0

    def has_next(self):
        return self.last < self.bookshelf.length()

    def next(self):
        try:
            book = self.bookshelf.get_book_at(self.last)
            self.last += 1
            return book
        except IndexError as e:
            print(e)
