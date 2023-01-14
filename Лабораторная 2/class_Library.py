BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __init__(self, books: list = None):
        self.books = books
        self.get_next_book_id()

    def get_next_book_id(self):
        if self.books is None:
            return 1
        else:
            book = self.books[-1]
            dict = book.__dict__
            lastid = dict["id"]
            return lastid+1

    def get_index_by_book_id(self, indx: int):
        books = self.books
        listofdicts = [book.__dict__ for book in books]
        listofids = [dict["id"] for dict in listofdicts]
        try:
            return listofids.index(indx)
        except ValueError:
            raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))
