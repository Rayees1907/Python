class BankAccount:

    def __init__(self, name, account_number, pin, balance):
        self.name = name
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance

    # INSTANCE METHOD
    # Deposit
    @deposit.setter
    def deposit(self, amount):
        if amount < 0:
            print("Please enter a valid amount, amount cannot be less than zero.")
        elif amount <= self.__balance:
            self.__balance += amount
        else:
            print("Error")
    
    #INSTANCE METHOD
    # Withdraw
    @withdraw.setter
    def withdraw(self, amount)