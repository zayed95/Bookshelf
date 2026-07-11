from schemas.books import Book

class DummyDatabase:

    books: dict[int, Book] = {}

db = DummyDatabase()

