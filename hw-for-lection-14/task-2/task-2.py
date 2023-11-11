class Restaurant:
    def __init__(self, name, cuisine, menu) -> None:
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru) -> None:
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish, qty):
        order_information = self.menu.get(dish)
        if not order_information:
            return "Dish not available"
        if order_information["quantity"] < qty or order_information["quantity"] == 0:
            return "Requested quantity not available"
        if order_information["quantity"] >= qty:
            order_price = order_information["price"] * qty
            self.menu[dish]["quantity"] -= qty
            return f"Your order price: {order_price}"
        


menu = {
    "burger": {"price": 5, "quantity": 10},
    "pizza": {"price": 10, "quantity": 20},
    "drink": {"price": 1, "quantity": 15},
}

mc = FastFood("McDonalds", "Fast Food", menu, True)

print(mc.order("burger", 5))  # 25
print(mc.order("burger", 15))  # Requested quantity not available
print(mc.order("soup", 5))  # Dish not available
print(mc.order("burger", 5))
print(mc.order("burger", 0))
