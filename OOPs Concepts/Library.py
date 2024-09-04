class Library:
    def __init__(self):
        self.noofBooks = 0
        self.books = []

    def addBooks(self,book):
        self.books.append(book)
        self.noofBooks = len(self.books)

    def showLibrary(self):
        print(f"Total number of books in the library: {self.noofBooks}")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

lib = Library()
lib.addBooks("Book1")
lib.addBooks("Book2")
lib.addBooks("Book3")
lib.addBooks("Book4")
lib.addBooks("Book5")
lib.showLibrary()