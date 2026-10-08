class Bankaccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        print(f"Balance: {self.__balance}")


cust1 = Bankaccount("rayees", 1200000)
cust1.__balance = 2000
print(cust1.__balance)      # this creates a new attribute but dosent change the existing attribute
cust1.get_balance()

cust1.deposit(25000)
cust1.get_balance()

cust1.withdraw(503002)
cust1.get_balance()