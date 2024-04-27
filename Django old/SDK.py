import booksSDK
from book import Book

def print_menu():
    print("""Choose an option:
    1.print all books
    2. add a book
    3.update a book
    4.delete a book
    """)

while True:
    print_menu()
    response = int(input())
    if response == 1:
        for book in booksSDK.get_books():
            print(book)
    elif response ==2:
        print("What is the name of the book?")
        title=input()
        print("How many pages is the book?")
        pages= int(input())
        book = Book(title, pages)       
        booksSDK.add_book(book)
        print("Adding a book")
    elif response == 3:
        print("What is the current title?")
        title = input()
        print("Current number of pages?")
        pages=input()

        book = Book(title, pages)

        print("What is the new title?")
        new_title= input()
        print("New numbwe of pages?")
        new_pages = input()

        print(booksSDK.update_book(book, new_title, new_pages))

        print("Updating books")
    elif response ==4:
        print("Title?")
        title= input()
        print("Pages?")
        pages= int(input())

        book= Book(title, pages)
        print(booksSDK.delete_book(book))
        print("Deleint ga bokdfs")
    else:
        print("Thanks for using our sweet app")
        break

import sqlite3
from book import Book

def cursor():
    return sqlite3.connect("books.db").cursor()

c=cursor()
c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
c.connection.close()

def add_book(book):
    c=cursor()

    with c.connection:
        c.execute('INSERT INTO books VALUES (?,?)', (book.title, book.pages))
    c.connection.close()
    return c.lastrowid

def get_books():
    c=cursor()
    books=[]

    with c.connection:    
        for book in c.execute("SELECT * FROM books"):
            books.append(Book(book[0], book[1]))
    c.connection.close()
    return books

    c.connection.close()

def get_book_by_title(title):
    c = cursor()
    with c.connection:
        c.execute("SELECT * FROM books WHERE title=?", (title,))
    data = c.fetchone()
    c.connection.close()
    if not data:
        return None

    return Book(data[0], data[1])

def update_book(book, new_title, new_pages):
    c = cursor()
    with c.connection: #don't forget this part.
        c.execute('UPDATE books SET title=?, pages=? WHERE title=? AND pages=?', 
        (new_title, new_pages, book.title, book.pages))
    book = get_book_by_title(book.title) #after commit
    c.connection.close()
    return book

def delete_book(book):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM books WHERE title=? AND pages=?', (book.title, book.pages))
    rows = c.rowcount
    c.connection.close()
    return rows

class Book():
    favs = [] #class

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return True

    #What happens when you pass object to print?
    def __str__(self):
        return f"{self.title}, {self.pages} pages long"

    #What happens when you use ==?
    def __eq__(self, other):
        if(self.title == other.title and self.pages == other.pages):
            return True
    
    #It's appropriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None

    def __repr__(self): #added to make list of items invoke str
        return self.__str__()