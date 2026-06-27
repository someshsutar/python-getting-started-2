from models import Customer, Order, Product
from payments import CreditCardPayment
from utils import Invoice


customer = Customer(1, "John")

laptop = Product(101, "Laptop", 55000)
mouse = Product(102, "Mouse", 1200)
keyboard = Product(103, "Keyboard", 2500)

order = Order(customer)

order.add_product(laptop, mouse, keyboard)

Invoice.print_invoice(order)

payment = CreditCardPayment()

payment.pay(order.total())