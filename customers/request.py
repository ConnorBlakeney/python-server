CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct",
      "animalId": 1,
      "email": "",
      "password": ""
    },
    {
      "id": 2,
      "name": "Anna Anderson",
      "address": "7054 Cherry Lane",
      "animalId": 2,
      "email": "",
      "password": ""
    },
    {
      "id": 3,
      "name": "Jenny Juice",
      "address": "7002 Chestnut Ct",
      "animalId": 3,
      "email": "",
      "password": ""
    },
    {
      "email": "test@test.com",
      "password": "me",
      "name": "connor blakeney",
      "id": 4
    }
]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer