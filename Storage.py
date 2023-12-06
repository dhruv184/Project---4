import csv

from Book import Book

class Data:

    @staticmethod

    def getData(filename):

        books = [ ]

        with open(filename , 'r') as file:

            reader = csv.reader(file)
            for row in reader:
                b = Book(row[0] , row[1] , row[2])
                books.append(b)

        return books        
    
    @ staticmethod

    def writeData(filename , rows):

        with open(filename , 'w' , newline = '') as file:

            writer = csv.writer(file)
            writer.writerows(rows)