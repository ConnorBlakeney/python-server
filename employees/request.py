import sqlite3
import json
from models import Employee

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
    # Open e connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's e Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id
        FROM employee e
        """)

        # Initialize an empty list to hold all animal representations
        employees = []

        # Convert rows of data into e Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            employee = Employee(row['name'],
                                row['location_id'],
                                row['id'])

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)


def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use e ? parameter to inject e variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        employee = Employee(data['name'],
                            data['location_id'],
                            data['id'])

        return json.dumps(employee.__dict__)


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
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break

def get_employees_by_location(location):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.location_id
        from Employee a
        WHERE e.location_id = ?
        """, ( location, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['name'],
                                row['location_id'],
                                row['id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)