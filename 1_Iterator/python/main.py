from Book import Book
from BookShelf import BookShelf


bookshelf = BookShelf()
bookshelf.append_book(Book("Around the World in 80 Days"))
bookshelf.append_book(Book("Bible"))
bookshelf.append_book(Book("Cinderella"))
bookshelf.append_book(Book("Daddy-Long-Legs"))
it = bookshelf.iterator()

while it.has_next():
    book = it.next()
    print(book.get_name())
