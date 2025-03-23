class Book(object):
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book is destroyed")

book = Book("Curso de Python", "Rodrigo Tadewald", 159)