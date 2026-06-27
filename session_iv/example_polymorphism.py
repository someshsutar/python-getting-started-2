from abc import ABC, abstractmethod

# =====================================================
# Abstract Class (Abstraction)
# =====================================================

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# =====================================================
# Method Overriding
# =====================================================

class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class WalletPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")


# =====================================================
# Method Overloading (Python Style)
# =====================================================

class Order:

    def __init__(self):
        self.products = []

    # Python doesn't support true method overloading.
    # Instead, *args allows a variable number of arguments.
    def add_product(self, *products):

        for product in products:
            self.products.append(product)

    def show_products(self):

        print("\nProducts in Order:")

        for product in self.products:
            print("-", product)


# =====================================================
# Polymorphism
# =====================================================

class PaymentService:

    def process_payment(self, payment_method, amount):
        payment_method.pay(amount)


# =====================================================
# Main Program
# =====================================================

def main():

    print("=" * 50)
    print("METHOD OVERLOADING DEMO")
    print("=" * 50)

    order = Order()

    # One product
    order.add_product("Laptop")

    # Two products
    order.add_product("Mouse", "Keyboard")

    # Three products
    order.add_product("Monitor", "USB Cable", "Headphones")

    order.show_products()

    amount = 65000

    print("\n" + "=" * 50)
    print("METHOD OVERRIDING + POLYMORPHISM DEMO")
    print("=" * 50)

    payment_service = PaymentService()

    payment_methods = [
        CreditCardPayment(),
        UPIPayment(),
        WalletPayment()
    ]

    for payment in payment_methods:
        payment_service.process_payment(payment, amount)


if __name__ == "__main__":
    main()