class Customer():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, name, address, customerId, email, password, unique_id):
        self.id = unique_id
        self.name = name
        self.address = address
        self.customerId = customerId
        self.email = email
        self.password = password
