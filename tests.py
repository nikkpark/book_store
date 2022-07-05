"""
Various tests to test functionality of books module.
"""
from books import PaperBook, AudioBook, Librarian

if __name__ == '__main__':
    def main():

        librarian = Librarian()

        book = librarian.create_book_item()
        if book:
            print('create_book_item: pass')
        else:
            print('create_book_item: fail')



    main()

