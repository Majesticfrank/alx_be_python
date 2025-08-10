class Book:
    def __init__(self, title, author ):
        self.title =title
        self .author =author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title,author, file_size):
      super().__init__(title, author)
      self.file_size = int(file_size)

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File size: {self.file_size}KB"



class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title,author)
        self.page_count=int(page_count)

    def __str__(self):
        return f"printBook: {self.title} by {self.author}, Page count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            return "only Book objects can be added to the library."
        



    def list_books(self):
        for book in self.books:
            print(book) 

