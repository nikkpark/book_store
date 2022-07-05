"""
The module contains classes to make book records
"""
import shelve


class Book:
    def __init__(self, name: str = None, author: str = None,
                 language: str = None, year: int = None, status: str = None):
        self.name = name
        self.author = author
        self.language = language
        self.year = year
        self.status = status

    def __gather_attrs(self):
        attrs = ['']
        for key in sorted(self.__dict__):
            attrs.append('%s: %s' % (key, getattr(self, key)))
        return '\n '.join(attrs)

    def __repr__(self):
        return '%s: %s' % (self.__class__.__name__, self.__gather_attrs())


class PaperBook(Book):
    def __init__(self, name: str = None, author: str = None,
                 language: str = None, year: int = None, status: str = None,
                 pages: int = 0, edition: str = None):
        Book.__init__(self, name, author, language, year, status)
        self.pages = pages
        self.edition = edition


class AudioBook(Book):
    def __init__(self, name: str = None, author: str = None,
                 language: str = None, year: int = None, status: str = None,
                 narrator: str = None, length: str = '00:00:00'):
        Book.__init__(self, name, author, language, year, status)
        self.narrator = narrator
        self.length = length


class Librarian:
    bookshelf_filename = 'bookshelf'

    def create_book_item(self):
        book_data = []

        booktype = input("Paper or Audio book?: ")

        book_data.append(input('Book name: '))
        book_data.append(input('Author:'))
        book_data.append(input('Language: '))
        while True:
            try:
                year = int(input('Year: '))
                break
            except ValueError:
                print('Year must be a number.')
                continue
        book_data.append(input('Status: '))

        if booktype == 'Paper':
            while True:
                try:
                    book_data.append(int(input('Pages: ')))
                    break
                except ValueError:
                    print('Number of pages must be a number.')
                    continue
            book_data.append(input('Edition: '))

            return PaperBook(*book_data)
        elif booktype == 'Audio':
            book_data.append(input('Narrator: '))
            book_data.append(input('Length(00:00:00): '))
            return AudioBook(*book_data)
        else:
            return None

    def shelve_book_item(self, book, filename=bookshelf_filename):
        with shelve.open(filename) as shelf:
            shelf[book.name] = book

    def read_book_item(self, book_name, filename=bookshelf_filename):
        with shelve.open(filename) as shelf:
            try:
                return shelf[book_name]
            except KeyError:
                print('No such book on shelf.')
                return None

    def update_book_item(self, book_name, filename=bookshelf_filename):
        with shelve.open(filename, writeback=True) as shelf:
            try:
                book = shelf[book_name]
                field_to_change = input("What info do you want to change?\n" + str(list(book.__dict__.keys())) + ' ')
                given_value = input(field_to_change + '| new value: ')
                setattr(book, field_to_change, given_value)

            except KeyError:
                print('No such book on shelf.')
                return None

    def delete_book_item(self, book_name, filename=bookshelf_filename):
        with shelve.open(filename) as shelf:
            try:
                del shelf[book_name]
                return True
            except KeyError:
                print('No such book on shelf. Nothing to delete.')
                return False


if __name__ == '__main__':
    def main():
        name = 'Awesome Book'
        author = 'J.P. Morgan'
        language = 'English'
        year = 1992
        status = 'Want to read'
        pages = 583
        edition = "Second"
        narrator = 'T.Hanks'
        length = '1:23:45'

        pbook = PaperBook(name, author, language, year, 'finished', pages, edition)
        abook = AudioBook(name, author, language, year, status, narrator, length)

        print(pbook)
        print(abook)

    main()
