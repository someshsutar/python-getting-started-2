Absolutely. An **Order Processing System** is one of the best examples for understanding OOP because it naturally contains multiple objects interacting with each other.

This project demonstrates **all major OOP concepts**:

* Classes & Objects
* Encapsulation
* Abstraction
* Inheritance
* Polymorphism
* Method Overriding
* Composition
* Python-style Overloading (`*args`)
* Properties (`@property`)
* Static Methods
* Class Methods

---

# Project Structure

```text
order_processing/

│
├── models.py
├── payments.py
├── utils.py
├── main.py
```

For learning, you can also keep everything in one file.

---

# Project Scenario

Suppose Amazon receives an order.

```text
Customer
      │
      ▼
Creates Order
      │
      ▼
Adds Products
      │
      ▼
Calculates Total
      │
      ▼
Chooses Payment Method
      │
      ▼
Processes Payment
      │
      ▼
Print Invoice
```

This workflow naturally uses all OOP concepts.

---

# Step 1. Product Class

## Demonstrates

* Class
* Object
* Encapsulation

```python
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
```

---

# Step 2. Customer Class

```python
class Customer:

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display(self):
        print(f"Customer : {self.name}")
```

---

# Step 3. Order Class

## Demonstrates

* Composition

An order HAS-A customer.

An order HAS-A list of products.

```python
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
```

Notice

```python
self.customer
```

means

> Order HAS-A Customer

and

```python
self.products
```

means

> Order HAS-MANY Products

This is **Composition**.

---

# Step 4. Payment Abstraction

## Demonstrates

Abstraction

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

No one can create

```python
Payment()
```

because it is abstract.

---

# Step 5. Different Payment Types

## Demonstrates

* Inheritance
* Method Overriding
* Polymorphism

### Credit Card

```python
class CreditCardPayment(Payment):

    def pay(self, amount):

        print(f"Paid ₹{amount} using Credit Card")
```

### UPI

```python
class UPIPayment(Payment):

    def pay(self, amount):

        print(f"Paid ₹{amount} using UPI")
```

### Wallet

```python
class WalletPayment(Payment):

    def pay(self, amount):

        print(f"Paid ₹{amount} using Wallet")
```

Each class overrides

```python
pay()
```

---

# Step 6. Invoice Utility

## Demonstrates

Static Method

```python
class Invoice:

    @staticmethod
    def print_invoice(order):

        print()

        print("=" * 40)

        print("INVOICE")

        order.display()

        print("=" * 40)
```

No object required.

Simply call

```python
Invoice.print_invoice(order)
```

---

# Step 7. Discount Utility

## Demonstrates

Class Method

```python
class Discount:

    tax = 18

    @classmethod
    def update_tax(cls, new_tax):

        cls.tax = new_tax
```

Changes tax for all instances.

---

# Step 8. Main Program

```python
customer = Customer(1, "John")

laptop = Product(101, "Laptop", 55000)
mouse = Product(102, "Mouse", 1200)
keyboard = Product(103, "Keyboard", 2500)

order = Order(customer)

order.add_product(laptop, mouse, keyboard)

Invoice.print_invoice(order)

payment = CreditCardPayment()

payment.pay(order.total())
```

Output

```text
========================================
INVOICE

----------------------------------------
Order ID : 1001

Customer : John

Laptop : ₹55000
Mouse : ₹1200
Keyboard : ₹2500

----------------------------------------
Total = 58700

========================================

Paid ₹58700 using Credit Card
```

---

# Polymorphism Example

Without changing the invoice code:

```python
payment = CreditCardPayment()
payment.pay(order.total())
```

or

```python
payment = UPIPayment()
payment.pay(order.total())
```

or

```python
payment = WalletPayment()
payment.pay(order.total())
```

Output changes automatically.

```text
Paid ₹58700 using Credit Card
```

```text
Paid ₹58700 using UPI
```

```text
Paid ₹58700 using Wallet
```

Same interface

```python
pay()
```

Different implementations.

That's **Polymorphism**.

---

# Inheritance Diagram

```text
                Payment (Abstract)
                     ▲
         ┌───────────┼────────────┐
         │           │            │
 CreditCard      UPI Payment   Wallet
```

---

# Composition Diagram

```text
Order
 │
 ├── Customer
 │
 └── Products
      │
      ├── Laptop
      ├── Mouse
      └── Keyboard
```

---

# Complete Object Relationship

```text
                    Customer
                        ▲
                        │
                  Order (HAS-A)
                        │
        ┌───────────────┴───────────────┐
        │                               │
    Product                         Product
        │                               │
     Laptop                         Mouse

                        │
                        ▼

             Payment (Abstract Class)

                ▲       ▲        ▲
                │       │        │
            Credit    UPI    Wallet

                        │
                        ▼

                   Invoice
```

---

# OOP Concepts Used

| OOP Feature              | Where Used                                                     |
| ------------------------ | -------------------------------------------------------------- |
| Class                    | `Product`, `Customer`, `Order`, `Payment`                      |
| Object                   | `customer`, `laptop`, `order`                                  |
| Encapsulation            | Private `__price` in `Product`                                 |
| Abstraction              | Abstract `Payment` class                                       |
| Inheritance              | Payment subclasses                                             |
| Method Overriding        | `pay()` in each payment type                                   |
| Polymorphism             | Switching payment implementations without changing client code |
| Composition              | `Order` contains `Customer` and `Product` objects              |
| Static Method            | `Invoice.print_invoice()`                                      |
| Class Method             | `Discount.update_tax()`                                        |
| Python-style Overloading | `Order.add_product(*products)` accepts one or many products    |
| Property                 | `Product.price` exposes read-only access to the private price  |


