from Book import Book 
from Storage import Data

class Library:

    def __init__(self):

        self.books = Data.getData('data.csv')

    def addBook(self , book):

        self.books.append(book)

    def getBooks(self):

        return self.books

    def findBooks(self, id):

        b = None

        for book in self.books:
            if book.id == id:
                b = book
                break

        return b        
    
    def saveData(self):

        rows = [ ]

        for b in self.books:
            row = [b.id , b.name , b.author]
            rows.append(row)

        Data.writeData('data.csv' , rows)

    def updateBook(self , book):

        b = self.findBooks(book.id)
        if isinstance(b, Book):
            b.name = book.name
            b.author = book.author
