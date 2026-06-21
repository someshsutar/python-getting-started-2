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