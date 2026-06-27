class Invoice:

    @staticmethod
    def print_invoice(order):

        print()

        print("=" * 40)

        print("INVOICE")

        order.display()

        print("=" * 40)

class Discount:

    tax = 18

    @classmethod
    def update_tax(cls, new_tax):

        cls.tax = new_tax