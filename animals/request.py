ANIMALS = [
    {
      "id": 1,
      "name": "Doodles",
      "breed": "Poodle",
      "customerId": 1,
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Sprinkles",
      "breed": "Shih Tzu",
      "customerId": 2,
      "locationId": 2
    },
    {
      "id": 3,
      "name": "Fuzzy",
      "breed": "Sheepdog",
      "customerId": 3,
      "locationId": 2
    },
    {
      "name": "Harry",
      "breed": "Great Dane",
      "locationId": 1,
      "treatment": "",
      "customerId": 2,
      "id": 4
    }
]


def get_all_animals():
    return ANIMALS

# Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal