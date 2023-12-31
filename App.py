import tkinter as tk

from Library import Library
from Book import Book

class appGUI:

    def __init__(self , master):

        self.master = master
        self.master.title("Books Management System")

        self.library = Library()
        
        self.label_id = tk.Label(master , text = "Book ID :")
        self.entry_id = tk.Entry(master)

        self.label_name = tk.Label(master , text = "Book Name :")
        self.entry_name = tk.Entry(master) 

        self.label_author = tk.Label(master , text = "Book Author :")
        self.entry_author = tk.Entry(master)

        self.display_box = tk.Text(master , height = 30 , width = 40)
        self.display_box.grid(row = 0 , column = 2 , rowspan = 9 , padx = 10 , pady = 5)

        self.button_view = tk.Button(master , text = "View Books" , command = self.view_books)
        self.button_add = tk.Button(master , text = "Add Book" , command = self.add_books)
        self.button_find = tk.Button(master , text = "Find Book" , command = self.find_book)
        self.button_save = tk.Button(master , text = "Save Data" , command = self.save_books)
        self.button_update = tk.Button(master , text = "Update Book" , command = self.update_book)
        self.button_delete = tk.Button(master , text = "Delete Product" , command = self.delete_book)
        self.button_exit = tk.Button(master , text = "Exit" , command = self.master.destroy)

        self.label_id.grid(row = 0 , column = 0 , padx = 10 , pady = 5)
        self.entry_id.grid(row = 0 , column = 1 , padx = 10 , pady = 5)

        self.label_name.grid(row = 1 , column = 0 , padx = 10 , pady = 5)
        self.entry_name.grid(row = 1 , column = 1 , padx = 10 , pady = 5)

        self.label_author.grid(row = 2 , column = 0 , padx = 10 , pady = 5)
        self.entry_author.grid(row = 2 , column = 1 , padx = 10 , pady = 5)

        self.button_view.grid(row = 3 , column = 0 , columnspan = 2 , pady = 10)
        self.button_add.grid(row = 4 , column = 0 , columnspan = 2 , pady = 10)
        self.button_find.grid(row = 5 , column = 0 , columnspan = 2 , pady = 10)
        self.button_save.grid(row = 6 , column = 0 , columnspan = 2 , pady = 10)
        self.button_update.grid(row = 7 , column = 0 , columnspan = 2 , pady = 10)
        self.button_delete.grid(row = 8 , column = 0 , columnspan = 2 , pady = 10)
        self.button_exit.grid(row = 9 , column = 0 , columnspan = 2 , pady = 10)

    def view_books(self):

        self.clear_entries()
        self.display_box.delete(1.0 , tk.END)
        self.display_box.insert(tk.END , "List of Books : \n")
        
        for b in self.library.getBooks():
            self.display_box.insert(tk.END , str(b) + "\n")
    
    def add_books(self):
        
        book_id = self.entry_id.get()
        book_name = self.entry_name.get()
        book_author = self.entry_author.get()

        book = Book(book_id, book_name, book_author)

        self.library.addBook(book)
        self.clear_entries()

    def find_book(self):

        book_id = self.entry_id.get()
        book = self.library.findBooks(book_id)
        self.display_box.delete(1.0, tk.END)  

        if isinstance(book, Book):
            self.display_box.insert(tk.END, str(book))
        else:
            self.display_box.insert(tk.END, f"Book with id = {book_id} is not found")

        self.clear_entries()

    def save_books(self):

        self.library.saveData()
        self.display_box.delete(1.0, tk.END)  
        self.display_box.insert(tk.END, "Data saved successfully")

    def update_book(self):

        book_id = self.entry_id.get()
        new_name = self.entry_name.get()
        new_author = self.entry_author.get()
        book = Book(book_id, new_name, new_author)

        self.library.updateBook(book)
        self.clear_entries()
    
    def delete_book(self):
        book_id = self.entry_id.get()
        book = self.library.findBooks(book_id)
        self.display_box.delete(1.0, tk.END)  
        if isinstance(book, Book):
            self.display_box.insert(tk.END, f"Deleting Product:\n{str(book)}\n")
            self.library.getBooks().remove(book)
            self.display_box.insert(tk.END, f"Product with id = {book_id} deleted successfully")
        else:
            self.display_box.insert(tk.END, f"Product with id = {book_id} is not found")
        self.clear_entries()    

    def clear_entries(self):

        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)

root = tk.Tk()
app = appGUI(root)
root.mainloop()