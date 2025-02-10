from typing import List
from LibraryInterface import LibraryInterface
from Book import Book


class Library(LibraryInterface):
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        self._books = [book for book in self._books if book.title != title]

    def list_books(self) -> List[Book]:
        return self._books
