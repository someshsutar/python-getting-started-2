import json
from pathlib import Path


def create_employee_data():

    return [
        {
            "id": 101,
            "name": "Someshwar",
            "city": "Pune",
            "salary": 120000
        },
        {
            "id": 102,
            "name": "John",
            "city": "Mumbai",
            "salary": 90000
        }
    ]


def write_json_file(file_path, data):

    try:

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print("JSON file created successfully")

    except Exception as ex:

        print(f"Write Error: {ex}")


def read_json_file(file_path):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except FileNotFoundError:

        print("File not found")

        return []

    except json.JSONDecodeError:

        print("Invalid JSON")

        return []

    except Exception as ex:

        print(ex)

        return []


def display_employees(employees):

    print("\nEmployee List")

    print("-" * 30)

    for employee in employees:

        print(
            f"{employee['id']} | "
            f"{employee['name']} | "
            f"{employee['city']} | "
            f"{employee['salary']}"
        )


def add_employee(employees):

    new_employee = {
        "id": 103,
        "name": "Mary",
        "city": "Bangalore",
        "salary": 110000
    }

    employees.append(new_employee)

    return employees


def main():

    folder = Path("data")

    folder.mkdir(exist_ok=True)

    file_path = folder / "employees.json"

    # Create data

    employees = create_employee_data()

    # Write file

    write_json_file(
        file_path,
        employees
    )

    # Verify file exists

    if file_path.exists():

        print("File exists")

    # Read file

    employees = read_json_file(
        file_path
    )

    display_employees(
        employees
    )

    # Update data

    employees = add_employee(
        employees
    )

    # Save updated data

    write_json_file(
        file_path,
        employees
    )

    print("\nUpdated Employee List")

    display_employees(
        employees
    )


if __name__ == "__main__":

    main()