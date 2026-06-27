class Product:

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.__price = price      # Private variable

    @property
    def price(self):
        return self.__price

    def display(self):
        print(f"{self.name} : ₹{self.__price}")


class Customer:

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display(self):
        print(f"Customer : {self.name}")


class Order:

    order_counter = 1000

    def __init__(self, customer):

        Order.order_counter += 1

        self.order_id = Order.order_counter
        self.customer = customer
        self.products = []

    def add_product(self, *products):

        self.products.extend(products)

    def total(self):

        return sum(product.price for product in self.products)

    def display(self):

        print("-" * 40)

        print("Order ID :", self.order_id)

        self.customer.display()

        print()

        for product in self.products:
            product.display()

        print("-" * 40)

        print("Total =", self.total())