# -----------------------------
# Standard Library Imports
# -----------------------------
import math
import random
from datetime import datetime
import os
import json

# -----------------------------
# Sample Data
# -----------------------------
numbers = [10, 5, 8, 3, 15]
names = ["Alice", "Bob", "Charlie"]

# -----------------------------
# Built-in Functions Demo
# -----------------------------
print("=== BUILT-IN FUNCTIONS ===")

print("Original numbers:", numbers)
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sorted list:", sorted(numbers))

print("Enumerating names:")
for index, name in enumerate(names):
    print(index, name)

print("Zip example:")
for n, num in zip(names, numbers):
    print(n, num)

print("Any > 10?", any(x > 10 for x in numbers))
print("All > 0?", all(x > 0 for x in numbers))

print()

# -----------------------------
# math module
# -----------------------------
print("=== MATH MODULE ===")
print("Square root of 64:", math.sqrt(64))
print("Factorial of 5:", math.factorial(5))
print("Value of pi:", math.pi)
print()

# -----------------------------
# random module
# -----------------------------
print("=== RANDOM MODULE ===")
print("Random integer (1-100):", random.randint(1, 100))
print("Random choice:", random.choice(names))
print()

# -----------------------------
# datetime module
# -----------------------------
print("=== DATETIME MODULE ===")
now = datetime.now()
print("Current Date & Time:", now)
print("Year:", now.year)
print("Month:", now.month)
print()

# -----------------------------
# os module
# -----------------------------
print("=== OS MODULE ===")
print("Current Working Directory:", os.getcwd())
print("Files in directory:", os.listdir())
print()

# -----------------------------
# json module
# -----------------------------
print("=== JSON MODULE ===")
student = {
    "id": 101,
    "name": "John",
    "marks": [80, 85, 90]
}

json_data = json.dumps(student, indent=4)
print("JSON Output:")
print(json_data)