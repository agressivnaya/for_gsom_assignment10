from Library import Book

def main():
    # Create a list of different books
    books = [
        Book("1984", "George Orwell", 1949, 5.71),
        Book("To Kill a Mockingbird", "Harper Lee", 1960, 9.71, True),
        Book("The Effective Executive", "Piter Drucker", 1966, 5.19),
        Book("Alice in Wonderland", "Lewis Caroll", 1865, 10.98),
        Book("Azazel", "Boris Akunin", 1998, 6.99, True)
    ]
    
    # Show information about each book
    print("Book Information:")
    for book in books:
        print(book.get_info())
        
    # Find and display the most expensive book
    most_expensive = Book.find_most_expensive(books)
    if most_expensive:
        print(f"\nMost Expensive Book:\n{most_expensive.get_info()}")
        
    # Set stoplist for a specific author
    author_to_censor = "Harper Lee"
    print(f"\nUncensoring books by {author_to_censor}...")
    for book in books:
        book.censor(author_to_censor, False)  # Setting stoplist to False
        
    # Show updated information about each book
    print("\nUpdated Book Information:")
    for book in books:
        print(book.get_info())
        
if __name__ == "__main__":
    main()