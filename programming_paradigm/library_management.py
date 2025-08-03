class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__is_checked_out =False
    
    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return f"{self.title} has been checked out by {self.author}."

class Library:
    def __init__(self):
         self.__books=[]


    def add_book(self, book):
        self.add_book.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                book.check_out()
            else:
                return f"No book with the title {title} is available in the library."
    def return_book(self):
         title = input("Enter the title of the book to check out: ")
         for book in self.books:
            if book.title == title:
                book.__is_checked_out = False
            else:
                return f"No book with the title {title} is available in the library."
    
    def list_available_books(self):

     available_books = [book for book in self._books if not book._is_checked_out]
     if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
     else:
            print("No books are currently available.")
