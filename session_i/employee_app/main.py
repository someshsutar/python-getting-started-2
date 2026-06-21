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