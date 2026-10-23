class BankAccount:
    def __init__(self, account_number, customer_name, pin, branch, initial_balance=0):
        # Public Attribute
        self.account_number = account_number

        # Protected Attribute (convention: single underscore)
        self._branch = branch

        # Private Attributes (convention: double underscore)
        self.__customer_name = customer_name
        self.__pin = pin
        self.__balance = initial_balance
        self.__failed_attempts = 0
        self.__is_locked = False
        self.__transactions = []

        # Record account opening transaction
        self.__record_transactions(f"Account created at {self._branch} branch")

    # ----------------------------------
    # PROPERTY : CUSTOMER NAME
    # ----------------------------------
    @property
    def customer_name(self):
        """Getter for customer name"""
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, new_name):
        """Setter with validation for customer name"""
        if isinstance(new_name, str) and new_name.strip():
            self.__customer_name = new_name.strip()
            self.__record_transactions(f"Customer name updated to: {self.__customer_name}")
        else:
            raise ValueError("Name cannot be empty.")

    # ----------------------------------
    # PROPERTY : BRANCH (PROTECTED)
    # ----------------------------------
    @property
    def branch(self):
        """Getter for branch (protected attribute)"""
        return self._branch

    @branch.setter
    def branch(self, new_branch):
        """Setter with validation for branch"""
        if isinstance(new_branch, str) and new_branch.strip():
            self._branch = new_branch.strip()
            self.__record_transactions(f"Branch transferred to: {self._branch}")
        else:
            raise ValueError("Branch name cannot be empty.")

    # -----------------------------------
    # READ ONLY PROPERTIES
    # -----------------------------------
    @property
    def balance(self):
        """Read-only property: balance cannot be directly modified"""
        return self.__balance

    @property
    def is_locked(self):
        """Read-only property: check if account is locked"""
        return self.__is_locked

    @property
    def pin(self):
        """Read-only property for PIN"""
        return self.__pin

    # -----------------------------------
    # PRIVATE HELPER METHODS
    # -----------------------------------
    def __record_transactions(self, message):
        """Private helper to record transaction logs"""
        self.__transactions.append(
            f"{message} | Balance: Rs. {self.__balance}"
        )

    def __verify_pin(self, entered_pin):
        """Private helper to authenticate PIN and track security attempts"""
        if self.__is_locked:
            print("❌ Security Alert: Account is LOCKED. Please unlock through your branch.")
            return False

        if entered_pin == self.__pin:
            self.__failed_attempts = 0
            return True
        else:
            self.__failed_attempts += 1
            remaining = 3 - self.__failed_attempts
            if self.__failed_attempts >= 3:
                self.__is_locked = True
                self.__record_transactions("Account LOCKED due to 3 consecutive failed PIN attempts")
                print("🚨 Security Alert: Account has been LOCKED after 3 failed PIN attempts!")
            else:
                print(f"❌ Incorrect PIN! Remaining attempts: {remaining}")
            return False

    # -----------------------------------
    # BANKING OPERATIONS (PUBLIC METHODS)
    # -----------------------------------
    def deposit(self, amount):
        """Deposit money into account"""
        if self.__is_locked:
            print("❌ Account is locked. Transactions cannot be processed.")
            return False

        if amount <= 0:
            print("❌ Invalid deposit amount. Amount must be greater than zero.")
            return False

        self.__balance += amount
        self.__record_transactions(f"Deposited: Rs. {amount:,.2f}")
        print(f"✅ Successfully deposited Rs. {amount:,.2f}. Current Balance: Rs. {self.__balance:,.2f}")
        return True

    def withdraw(self, amount, pin):
        """Withdraw money from account after PIN verification"""
        if not self.__verify_pin(pin):
            return False

        if amount <= 0:
            print("❌ Invalid withdrawal amount. Amount must be greater than zero.")
            return False

        if amount > self.__balance:
            print(f"❌ Insufficient funds! Current Balance: Rs. {self.__balance:,.2f}")
            return False

        self.__balance -= amount
        self.__record_transactions(f"Withdrew: Rs. {amount:,.2f}")
        print(f"✅ Successfully withdrew Rs. {amount:,.2f}. Current Balance: Rs. {self.__balance:,.2f}")
        return True

    def change_pin(self, old_pin, new_pin):
        """Change PIN after authenticating old PIN and validating new PIN"""
        if not self.__verify_pin(old_pin):
            print("❌ Failed to change PIN: Old PIN is incorrect.")
            return False

        if not (isinstance(new_pin, int) or (isinstance(new_pin, str) and str(new_pin).isdigit())):
            print("❌ PIN must contain digits only.")
            return False

        if len(str(new_pin)) != 4:
            print("❌ PIN must be a 4-digit number.")
            return False

        if old_pin == new_pin:
            print("❌ New PIN must be different from the old PIN.")
            return False

        self.__pin = new_pin
        self.__record_transactions("PIN changed successfully")
        print("✅ PIN changed successfully!")
        return True

    def unlock_account(self, branch_name):
        """Unlocks account via branch verification (demonstrating protected attribute usage)"""
        if not self.__is_locked:
            print("ℹ️ Account is not locked.")
            return True

        if branch_name.strip().lower() == self._branch.strip().lower():
            self.__is_locked = False
            self.__failed_attempts = 0
            self.__record_transactions("Account unlocked via branch verification")
            print(f"✅ Account {self.account_number} successfully unlocked by branch '{self._branch}'!")
            return True
        else:
            print("❌ Branch verification failed. Account remains locked.")
            return False

    def display_transactions(self):
        """Displays complete transaction statement"""
        print(f"\n{'=' * 20} TRANSACTION STATEMENT {'=' * 20}")
        print(f"Account: {self.account_number} | Customer: {self.__customer_name}")
        print("-" * 63)
        if not self.__transactions:
            print("No transactions found.")
        else:
            for idx, txn in enumerate(self.__transactions, start=1):
                print(f" {idx}. {txn}")
        print("-" * 63)
        print(f"Closing Balance: Rs. {self.__balance:,.2f}")
        print(f"{'=' * 63}\n")

    def account_details(self):
        """Displays account summary"""
        status = "🔒 Locked" if self.__is_locked else "🟢 Active"
        print(f"\n{'-' * 18} ACCOUNT DETAILS {'-' * 18}")
        print(f"Account Number  : {self.account_number}")
        print(f"Customer Name   : {self.customer_name}")
        print(f"Branch          : {self.branch}")
        print(f"Account Balance : Rs. {self.__balance:,.2f}")
        print(f"Account Status  : {status}")
        print(f"{'-' * 53}\n")


if __name__ == "__main__":
    print("\n================ BANKING ENCAPSULATION DEMO ================")

    # 1. Account Creation
    print("\n--- 1. Creating Bank Account ---")
    account = BankAccount(account_number=1001234567, customer_name="Syed Rayees", pin=4321, branch="Downtown")
    account.account_details()

    # 2. Properties (Getter / Setter)
    print("--- 2. Testing Property Getters and Setters ---")
    print(f"Current Name: {account.customer_name}")
    account.customer_name = "Syed Mohammad Rayees"
    print(f"Updated Name: {account.customer_name}")

    # 3. Deposit
    print("\n--- 3. Testing Deposits & Read-Only Balance ---")
    account.deposit(50000)
    print(f"Balance via read-only property: Rs. {account.balance:,.2f}")

    # 4. Withdraw with PIN
    print("\n--- 4. Testing Withdrawal with Valid PIN ---")
    account.withdraw(12000, pin=4321)

    # 5. Security & Account Locking
    print("\n--- 5. Testing Security: Failed PIN Attempts & Account Lock ---")
    account.withdraw(5000, pin=1111)  # Attempt 1
    account.withdraw(5000, pin=2222)  # Attempt 2
    account.withdraw(5000, pin=3333)  # Attempt 3 -> Triggers Lock!

    print(f"\nIs account locked? {account.is_locked}")
    print("Attempting withdrawal while locked with correct PIN:")
    account.withdraw(5000, pin=4321)

    # 6. Unlocking Account
    print("\n--- 6. Unlocking Account via Branch Verification ---")
    account.unlock_account(branch_name="Downtown")

    # 7. Changing PIN
    print("\n--- 7. Changing PIN ---")
    account.change_pin(old_pin=4321, new_pin=9876)

    # 8. Testing Withdrawal with New PIN
    print("\n--- 8. Testing Withdrawal with New PIN ---")
    account.withdraw(5000, pin=9876)

    # 9. Transaction Statement
    print("\n--- 9. Transaction History ---")
    account.display_transactions()