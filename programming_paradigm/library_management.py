class Book:
    def __init__(self,title,author,is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out

    def check_out(self):
        if self._book == self.check_out:
            return True

        else:
            return False
    
    def return_book(self):
        self.return_book -= Book

class Library(Book):
    def __init__(self):
        self._books = []

    def __init__(self , title, author, is_checked_out , book):
        super().__init__(title, author, is_checked_out)
        self._books = book
        
    def add_book(self):
        self._books.append(self._books)
        print(f"You have added {self.title} by {self.author}")

    def checkout_book(self):
        self.checkout_book.remove(self._books)
        return f"Available books after checking out '1984'\n {self.title}"

    def return_book(self):
        self.return_book.append(self._books)
        return f"Available books after returing '1984':\n {self.title}\n {self.author}"

    def list_available_books(self):
        return f"Available books after setup:\n {self.title}\n {self.author}"