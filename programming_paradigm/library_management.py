class Book:
    def __init__(self,title,author,is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out

class Library(Book):
    def __init__(self , title, author, is_checked_out):
        super().__init__(title, author, is_checked_out)

    def __init__(self,book):
        self._book = book
        
    def add_book(self,book):
        self.add_book += book
        print(f"You have added {self.title} by {self.author}")

    def checkout_book(self,book):
        self.checkout_book -= book
        return f"Available books after checking out '1984'\n {self.title}"

    def return_book(self,book):
        self.return_book += book
        return f"Available books after returing '1984':\n {self.title}\n {self.author}"

    def list_available_books(self):
        return f"Available books after setup:\n {self.title}\n {self.author}"