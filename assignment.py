# Base class representing a general Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Inheritance - FictionBook class inherits from Book
class FictionBook(Book):
    def __init__(self, title, author, pages, genre):
        super().__init__(title, author, pages)
        self.genre = genre  # Additional attribute specific to FictionBook

    def describe(self):
        super().describe()
        print(f"Genre: {self.genre}")

    def read(self):
        print(f"You're reading a fiction book: {self.title} by {self.author}. Enjoy the adventure!")

# Inheritance - NonFictionBook class inherits from Book
class NonFictionBook(Book):
    def __init__(self, title, author, pages, field):
        super().__init__(title, author, pages)
        self.field = field  # Additional attribute specific to NonFictionBook

    def describe(self):
        super().describe()
        print(f"Field: {self.field}")

    def read(self):
        print(f"You're reading a non-fiction book: {self.title} by {self.author}. Learning is fun!")

# Example usage
fiction_book = FictionBook("The Great Adventure", "John Doe", 300, "Fantasy")
non_fiction_book = NonFictionBook("The Science of Learning", "Jane Smith", 200, "Psychology")

# Describing books
fiction_book.describe()
print("---")
non_fiction_book.describe()

# 
# #Reading books
fiction_book.read()
non_fiction_book.read()
