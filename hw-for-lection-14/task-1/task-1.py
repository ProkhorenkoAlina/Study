class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        return f"Author: {self.author}, name: {self.name}, price: {self.price}, quantity: {self.quantity}"


book = Book("Alice's Adventures in Wonderland", 500, 3, "Lewis Carroll")

print(book.read())