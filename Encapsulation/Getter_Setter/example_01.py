# A getter is a method used to get/read the value of private data.
# A setter is a method used to set/change the value of private data.
# Getter_Setter: Used to access/read private data.
# Setter: Used to modify/update private data.

class User:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance        # private attribute

    # Getter_Setter
    def get_balance(self):
        print(f"Balance: {self.__balance}")

    # Setter
    def set_balance(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Error")


user1 = User("rayees", 1000)
user1.get_balance()
user1.set_balance(20000)
user1.get_balance()