class Person:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class CustomerModel(Person):
    def __init__(self, name, email, password, balance=0.0):
        super().__init__(name, email, password)
        self.__balance = balance  # Private

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount
