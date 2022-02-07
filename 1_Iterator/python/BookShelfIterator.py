from Iterator import Iterator


class BookShelfIterator(Iterator):

    def __init__(self, bookshelf):
        self._bookshelf = bookshelf
        self._last = 0

    def has_next(self):
        return self._last < self._bookshelf.length()

    def next(self):
        try:
            book = self._bookshelf.get_book_at(self._last)
            self._last += 1
            return book
        except IndexError as e:
            print(e)
