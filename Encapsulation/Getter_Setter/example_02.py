# A getter is a method used to get/read the value of private data.
# A setter is a method used to set/change the value of private data.
# Getter: Used to access/read private data.
# Setter: Used to modify/update private data.

class User:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance        # private attribute

    # Getter
    @property
    def balance(self):
        print(f"Balance: {self.__balance}")

    # Setter
    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Error")


user1 = User("rayees", 1000)
print(user1.balance)

user1.balance = 20000
print(user1.balance)