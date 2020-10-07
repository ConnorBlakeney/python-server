EMPLOYEES = [
    {
      "id": 1,
      "name": "Big Hal",
      "locationId": 2,
      "animalId": 1
    },
    {
      "id": 2,
      "name": "Big Abe",
      "locationId": 2,
      "animalId": 2
    },
    {
      "id": 3,
      "name": "Big Jude",
      "locationId": 1,
      "animalId": 1
    },
    {
      "id": 4,
      "name": "Big Germ",
      "locationId": 1,
      "animalId": 2
    },
    {
      "name": "Jake",
      "locationId": 1,
      "animalId": 3,
      "id": 5
    }
]


def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee