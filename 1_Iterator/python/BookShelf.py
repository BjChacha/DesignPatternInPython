from Aggregate import Aggregate
from BookShelfIterator import BookShelfIterator


class BookShelf(Aggregate):

    def __init__(self):
        self.books = []

    def get_book_at(self, index):
        try:
            return self.books[index]
        except IndexError as e:
            print(e)

    def append_book(self, book):
        self.books.append(book)

    def length(self):
        return len(self.books)

    def iterator(self):
        return BookShelfIterator(self)
