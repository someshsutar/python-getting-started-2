Here's a practical example that demonstrates:

* Creating **modules**
* Creating **packages**
* Using `__init__.py`
* Importing modules in different ways
* Using `main()`

We'll build a simple Employee Management application.

# Project Structure

```text
employee_app/

main.py

services/
│
├── __init__.py
├── employee_service.py
└── salary_service.py

utils/
│
├── __init__.py
└── validator.py
```

---

# 1. services/employee_service.py

```python
# services/employee_service.py

def get_employee():

    return {
        "id": 101,
        "name": "Someshwar",
        "city": "Pune"
    }


def display_employee(employee):

    print("\nEmployee Information")

    for key, value in employee.items():
        print(f"{key}: {value}")
```

---

# 2. services/salary_service.py

```python
# services/salary_service.py

def calculate_bonus(salary):

    return salary * 0.20


def calculate_tax(salary):

    return salary * 0.10
```

---

# 3. utils/validator.py

```python
# utils/validator.py

def is_valid_salary(salary):

    return salary > 0
```

---

# 4. services/**init**.py

`__init__.py` tells Python that this directory is a package.

It can also expose selected functions.

```python
# services/__init__.py

from .employee_service import (
    get_employee,
    display_employee
)

from .salary_service import (
    calculate_bonus,
    calculate_tax
)
```

Notice the `.`

```python
from .employee_service import ...
```

means:

> Import from another module inside the same package.

---

# 5. utils/**init**.py

```python
# utils/__init__.py

from .validator import is_valid_salary
```

---

# 6. main.py

```python
# main.py

from services import (
    get_employee,
    display_employee,
    calculate_bonus,
    calculate_tax
)

from utils import is_valid_salary


def main():

    employee = get_employee()

    display_employee(employee)

    salary = 120000

    if is_valid_salary(salary):

        bonus = calculate_bonus(salary)

        tax = calculate_tax(salary)

        print("\nSalary Information")

        print(f"Salary : {salary}")

        print(f"Bonus  : {bonus}")

        print(f"Tax    : {tax}")

    else:

        print("Invalid Salary")


if __name__ == "__main__":
    main()
```

# Output

```text
Employee Information

id: 101
name: Someshwar
city: Pune

Salary Information

Salary : 120000

Bonus  : 24000.0

Tax    : 12000.0
```

# What is `__init__.py` actually doing?

Without `__init__.py`

You would write:

```python
from services.employee_service import get_employee
from services.employee_service import display_employee
from services.salary_service import calculate_bonus
from services.salary_service import calculate_tax
```

With `__init__.py`

```python
from services import (
    get_employee,
    display_employee,
    calculate_bonus,
    calculate_tax
)
```

It acts as a **public entry point** for the package.

---

# Another common use of `__init__.py`

You can initialize package-level variables.

```python
# services/__init__.py

print("Loading Services Package...")

VERSION = "1.0.0"
```

Then:

```python
import services

print(services.VERSION)
```

Output:

```text
Loading Services Package...
1.0.0
```

Notice:

* `__init__.py` runs only once when the package is first imported.

---

# Python execution flow

When Python executes:

```python
from services import get_employee
```

Python does:

```text
1. Locate services folder

2. Execute services/__init__.py

3. Load employee_service.py

4. Expose get_employee
```

---

# Comparison with .NET

| Python                | .NET                                                               |
| --------------------- | ------------------------------------------------------------------ |
| `employee_service.py` | EmployeeService.cs                                                 |
| `services` folder     | Namespace/Project                                                  |
| `__init__.py`         | Public exports configuration (similar concept to a library facade) |
| `import`              | `using`                                                            |
| `main.py`             | Program.cs                                                         |

---

## Modern note

Starting with Python 3.3, folders can work as **namespace packages** even without `__init__.py`.

However, `__init__.py` is still commonly used because it:

* Makes imports cleaner
* Defines a package's public API
* Performs package initialization
* Improves code organization

For learning Python and building medium-to-large applications, it's still a good practice to understand and use `__init__.py`.
