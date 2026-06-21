# Intermediate Python Sessions

## **Session 1: Modules & Packages**
- Why use modules? (reuse, clarity, maintainability)
- Importing built-in modules (`math`, `random`)
- Creating custom modules
- Packages and `__init__.py`

**Examples:**
```python
import math
print(math.sqrt(16))

# mymodule.py
def greet(name):
    return f"Hello, {name}"

# main.py
import mymodule
print(mymodule.greet("Someshwar"))
```

**Exercises:**
- Import `random` and generate a random number between 1–100.
- Create a custom module with a function that returns the cube of a number.

**Mini Quiz:**
1. What keyword is used to bring a module into your program?  
2. True/False: You can import your own `.py` files as modules.  
3. What is the purpose of `__init__.py` in a package?

---

## **Session 2: File Handling**
- Opening files with `open()`
- Reading and writing text files
- CSV and JSON basics
- Using `with` for safe file handling

**Examples:**
```python
with open("notes.txt", "w") as f:
    f.write("Hello, Python learners!")

with open("notes.txt", "r") as f:
    print(f.read())
```

**Exercises:**
- Write a program that saves user input into a file.
- Read a CSV file and print each row.

**Mini Quiz:**
1. What mode is used to open a file for writing?  
2. Why is `with open(...)` preferred over `open()` alone?  
3. Which module helps you work with JSON files?

---

## **Session 3: Error Handling**
- Common errors (SyntaxError, ValueError, FileNotFoundError)
- Using `try/except`
- Raising exceptions with `raise`
- Cleanup with `finally`

**Examples:**
```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
```

**Exercises:**
- Write a program that asks for a number and handles invalid input.
- Create a function that raises an exception if a negative number is passed.

**Mini Quiz:**
1. What keyword is used to catch exceptions?  
2. What does `finally` do in error handling?  
3. True/False: You can raise your own exceptions in Python.

---

## **Session 4: Object-Oriented Programming**
- Classes and objects
- Attributes and methods
- Inheritance and polymorphism
- Encapsulation

**Examples:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

dog = Dog("Buddy")
dog.speak()
```

**Exercises:**
- Create a `Car` class with attributes `brand` and `year`.
- Add a method `drive()` that prints a message.
- Extend the class into `ElectricCar` with an extra attribute `battery`.

**Mini Quiz:**
1. What method initializes attributes in a class?  
2. True/False: A subclass can override methods of its parent class.  
3. What is encapsulation in OOP?

---

## **Session 5: Libraries**
- Standard libraries: `datetime`, `math`, `random`
- Third-party libraries: `requests`, `pandas`
- Installing with `pip`

**Examples:**
```python
import datetime
print(datetime.datetime.now())

import requests
response = requests.get("https://api.github.com")
print(response.status_code)
```

**Exercises:**
- Use `datetime` to print today’s date.
- Use `requests` to fetch data from a public API and print the response.

**Mini Quiz:**
1. Which command installs external libraries?  
2. Name one standard library in Python.  
3. True/False: `pandas` is part of Python’s standard library.

---

## **Session 6: Mini Project — Text-Based Game**
- Project overview
- Using functions and modules
- Handling user input and errors
- Saving game progress to a file

**Examples (starter code):**
```python
def start_game():
    print("Welcome to the Adventure!")
    choice = input("Do you go left or right? ")
    if choice == "left":
        print("You found a treasure!")
    else:
        print("You fell into a trap!")

start_game()
```

**Exercises:**
- Expand the game with multiple levels.
- Save player progress to a file.
- Add error handling for invalid inputs.

**Mini Quiz:**
1. What Python feature helps organize game logic into reusable blocks?  
2. True/False: You can save game progress using file handling.  
3. What keyword is used to define a function?
