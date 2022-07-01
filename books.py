"""
The module contains classes to make book records
"""


class Book:
    def __init__(self, name: str = None, author: str = None,
                 language: str = None, year: int = None, status: str = None):
        self.name = name
        self.author = author
        self.language = language
        self.year = year
        self.status = status

    def gather_attrs(self):
        attrs = ['']
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return '\n '.join(attrs)

    def __repr__(self):
        return '%s: %s' % (self.__class__.__name__, self.gather_attrs())

    def create_book(self):
        pass

    def read_book(self):
        pass

    def update_book(self):
        pass

    def delete_book(self):
        pass


class PaperBook(Book):
    def __init__(self, name: str = None, author: str = None,
                 language: str = None, year: int = None, status: str = None,
                 pages: int = 0, isbn: str = None, edition: str = None):
        Book.__init__(self, name, author, language, year, status)
        self.pages = pages
        self.isbn = isbn
        self.edition = edition


class AudioBook(Book):
    def __init__(self, name: str = None, author: str = None,
                 language: str = None, year: int = None, status: str = None,
                 narrator: str = None, length: str = None):
        Book.__init__(self, name, author, language, year, status)
        self.narrator = narrator
        self.length = length


if __name__ == '__main__':
    name = 'Awesome Book'
    author = 'J.P. Morgan'
    language = 'English'
    year = 1992
    status = 'Want to read'
    pages = 583
    isbn = 'i1y2jhho440493'
    edition = "Second"

    book = PaperBook(name, author, language, year, status, pages, isbn, edition)
    print(book)
