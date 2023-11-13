from typing import Optional
from collections import defaultdict


def default_zero():
    return 0


class Product:
    def __init__(self, name: str, descriptiotn: str, price: float) -> None:
        self.name = name
        self.description = descriptiotn
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}"


class Warehouse:
    def __init__(self) -> None:
        self.stock = defaultdict(default_zero)

    def add_product(self, product: Product, qty: int):
        self.stock[product] += qty

    def view_stock(self):
        return ", ".join(
            sorted(f"{product.name}: {qty}" for product, qty in self.stock.items())
        )


class ShoppingCart(dict):

    def add(self, product: Product, qty: int):
        self[product] = qty


class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product: Product, qty: int):
        self.shopping_cart.add(product, qty)

    def view_cart(self) -> Optional[str]:
        if not self.shopping_cart:
            return None
        return ", ".join(
            sorted(
                f"{product.name}: {qty}"
                for product, qty in self.shopping_cart.items()
            )
        )


class Order:
    def __init__(self, user: User, warehouse: Warehouse) -> None:
        self.user = user
        self.warehouse = warehouse

    def place_order(self):
        for product, qty in self.user.shopping_cart.items():
            if stock_qty := self.warehouse.stock.get(product):
                if stock_qty < qty:
                    raise ValueError(
                        f"Order can't be placed {qty} items of {product} is not available."
                    )
            else:
                raise ValueError(f"Product {product} is not available in stock.")

        for product, qty in self.user.shopping_cart.items():
            self.warehouse.stock[product] -= qty

        self.user.shopping_cart.clear()


# Create warehouse and products
warehouse = Warehouse()
apple = Product("Apple", "Fresh Red Apple", 0.5)  # name, description, price
banana = Product("Banana", "Fresh Yellow Banana", 0.3)

# Add products to warehouse
warehouse.add_product(apple, 100)  # 100 apples in warehouse
warehouse.add_product(banana, 150)  # 150 bananas in warehouse

# Create a user
user = User("John Doe", "john.doe@example.com")

# User adds items to cart
user.add_to_cart(apple, 5)
user.add_to_cart(banana, 10)


print(user.view_cart())  # Output: Apple: 5, Banana: 10
assert user.view_cart() == "Apple: 5, Banana: 10"

# User places an order
order = Order(user, warehouse)
order.place_order()

# User views items in cart after order is placed (should be empty)
print(user.view_cart())  # Output: None
assert user.view_cart() is None

# View stock after order is placed
print(warehouse.view_stock())  # Output: Apple: 95, Banana: 140
assert warehouse.view_stock() == "Apple: 95, Banana: 140"
