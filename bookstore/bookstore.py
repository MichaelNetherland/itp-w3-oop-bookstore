class Bookstore(object):
    def __init__(self,name):
      self.name = name
      self.booklist = []
      
    def add_book(self,book):
      self.booklist.append(book)
    
    def get_books(self):
      return self.booklist
    
    def search_books(self,author=None, title=None):
        ilovelists = []
        if author is not None and title is None:
            for book in self.booklist:
                if author == book.author:
                    ilovelists.append(book)
        elif author is None and title is not None:
            for book in self.booklist:
                if title.lower() in book.title.lower():
                    ilovelists.append(book)
        elif author is not None and title is not None:
            for book in self.booklist:
                if author == book.author and title in book.title:
                    ilovelists.append(book)
        return ilovelists
            
        
class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
    
    def get_books(self):
        return self.books

    def add_book(self,book):
        self.books.append(book)

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.author.add_book(self)    
    
        