class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Book name:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        Publisher.__init__(self, name)
        self.title = title
        self.author = author

    def display(self):
        print("Author name:", self.author)
        print("Title name:", self.title)


class Python(Book):
    def __init__(self, name, title, author, price, no_of_page):
        Book.__init__(self, name, title, author)
        self.price = price
        self.no_of_page = no_of_page

    def display(self):
        Publisher.display(self)
        Book.display(self)
        print("Price amount:", self.price)
        print("Number of pages:", self.no_of_page)


n = input("Publisher name: ")
t = input("Enter the title: ")
a = input("Enter the author name: ")
p = float(input("Enter the price of the book: "))
np = int(input("Enter the number of pages: "))

obj = Python(n, t, a, p, np)
obj.display()
