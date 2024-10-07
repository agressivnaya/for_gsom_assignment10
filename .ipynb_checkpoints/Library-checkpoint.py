class Book:
    def __init__(self, title, author, year, price, stoplist=False):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist

    def get_info(self):
        return f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Price: ${self.price:.2f}, Stoplist: {self.stoplist}"

    @staticmethod
    def find_most_expensive(books):
        if not books:
            return None  # Return None if the list is empty
        most_expensive_book = max(books, key=lambda book: book.price)
        return most_expensive_book

    def set_stoplist(self, value):
        self.stoplist = value

    def censor(self, author_name, value):
        if self.author == author_name:
            self.stoplist = value