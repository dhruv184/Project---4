class Book:

    def __init__(self , bookID , bookName , Author):

        self.id = bookID
        self.name = bookName
        self.author = Author

    def __str__(self):

        return f"ID : {self.id}\nName : {self.name}\nAuthor : {self.author}\n"    