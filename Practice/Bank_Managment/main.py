class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance


    # account holder info
    def account_details(self):
        print("Account Holder: ", self.account_holder)
        print("Account Number: ", self.account_number)
        print("Account Balance: ", self.balance)


    # deposit info
    def deposit(self, deposit_amount):
        print("Deposited Amount: ", deposit_amount)
        self.balance += deposit_amount
        print("Balance: ", self.balance)


    # withdraw info
    def withdraw(self, withdraw_amount):
        print("Withdraw Amount: ", withdraw_amount)
        self.balance -= withdraw_amount
        print("Balance: ", self.balance)


account1 = BankAccount("Rayees", 234234523556, 0)
account1.deposit(500000)
account1.account_details()
account1.withdraw(4000)