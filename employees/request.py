# import employees


EMPLOYEES = [
    {
      "id": 1,
      "name": "Big Hal",
      "locationId": 2,
    },
    {
      "id": 2,
      "name": "Big Abe",
      "locationId": 2,
    },
    {
      "id": 3,
      "name": "Big Jude",
      "locationId": 1,
    },
    {
      "id": 4,
      "name": "Big Germ",
      "locationId": 1,
    },
    {
      "name": "Jake",
      "locationId": 1,
      "id": 5
    }
]


def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)