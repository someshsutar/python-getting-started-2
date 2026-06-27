from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):

    def pay(self, amount):

        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(Payment):

    def pay(self, amount):

        print(f"Paid ₹{amount} using UPI")


class WalletPayment(Payment):

    def pay(self, amount):

        print(f"Paid ₹{amount} using Wallet")