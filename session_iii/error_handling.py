from pathlib import Path


# ----------------------------------------
# Custom Exception
# ----------------------------------------

class InvalidSalaryError(Exception):
    pass


# ----------------------------------------
# Business Logic
# ----------------------------------------

def calculate_bonus(salary):

    if salary <= 0:

        raise InvalidSalaryError(
            "Salary must be greater than zero"
        )

    return salary * 0.20


# ----------------------------------------
# File Handling
# ----------------------------------------

def read_employee_file():

    file_path = Path("employees.txt")

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

            print("\nEmployee File Content:")

            print(content)

    except FileNotFoundError:

        print(
            "\nemployees.txt not found"
        )

    except Exception as ex:

        print(
            f"File Error: {ex}"
        )


# ----------------------------------------
# Main Program
# ----------------------------------------

def main():

    try:

        salary_text = input(
            "Enter employee salary: "
        )

        salary = int(
            salary_text
        )

        bonus = calculate_bonus(
            salary
        )

    except ValueError:

        print(
            "\nInvalid number entered"
        )

    except InvalidSalaryError as ex:

        print(
            f"\nBusiness Error: {ex}"
        )

    except Exception as ex:

        print(
            f"\nUnexpected Error: {ex}"
        )

    else:

        print(
            "\nSalary accepted"
        )

        print(
            f"Bonus = {bonus}"
        )

    finally:

        print(
            "\nSalary processing completed"
        )

    # Demonstrate safe file handling

    read_employee_file()


# ----------------------------------------
# Program Entry Point
# ----------------------------------------

if __name__ == "__main__":

    main()