from logger import logger
from LibraryInterface import LibraryInterface
from Book import Book


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.list_books()
        if books:
            for book in books:
                logger.info(book)
        else:
            logger.error("No books in the library.")
