"""
Bank Management System (CLI)
An interactive console banking application demonstrating Encapsulation.
"""

from main import BankAccount


def main_menu():
    print("""
=================================================
             🏦 PYTHON SECURE BANK ATM
=================================================
 1. View Account Details
 2. Check Balance
 3. Deposit Money
 4. Withdraw Money
 5. Change Customer Name
 6. Change PIN
 7. View Transaction Statement
 8. Unlock Account (Branch Verification)
 9. Exit
=================================================
""")


def run_bank_system():
    print("\n👋 Welcome to Python Secure Bank!")
    print("Let's first set up your bank account.\n")

    while True:
        try:
            acc_num = int(input("Enter 10-digit Account Number: "))
            name = input("Enter Account Holder Name: ").strip()
            if not name:
                print("❌ Name cannot be empty.")
                continue

            pin_input = input("Set a 4-digit PIN: ").strip()
            if not (pin_input.isdigit() and len(pin_input) == 4):
                print("❌ PIN must be a 4-digit number.")
                continue
            pin = int(pin_input)

            branch = input("Enter Branch Name (e.g. Downtown, Uptown): ").strip()
            if not branch:
                print("❌ Branch cannot be empty.")
                continue

            opening_balance = float(input("Enter Initial Deposit Amount (Rs.): ") or "0")
            if opening_balance < 0:
                print("❌ Initial deposit cannot be negative.")
                continue

            account = BankAccount(
                account_number=acc_num,
                customer_name=name,
                pin=pin,
                branch=branch,
                initial_balance=opening_balance
            )
            print("\n🎉 Account successfully created!")
            account.account_details()
            break
        except ValueError as e:
            print(f"❌ Input error: {e}. Please try again.\n")

    # Main Interactive Loop
    while True:
        main_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            account.account_details()

        elif choice == "2":
            # Using read-only property
            print(f"\n💰 Current Available Balance: Rs. {account.balance:,.2f}")

        elif choice == "3":
            try:
                amount = float(input("\nEnter amount to deposit: Rs. "))
                account.deposit(amount)
            except ValueError:
                print("❌ Please enter a valid numerical amount.")

        elif choice == "4":
            try:
                amount = float(input("\nEnter amount to withdraw: Rs. "))
                pin_attempt = int(input("Enter your 4-digit PIN: "))
                account.withdraw(amount, pin=pin_attempt)
            except ValueError:
                print("❌ Invalid input. Please enter valid numbers.")

        elif choice == "5":
            new_name = input("\nEnter updated Customer Name: ").strip()
            try:
                account.customer_name = new_name
                print(f"✅ Customer name updated to: {account.customer_name}")
            except ValueError as err:
                print(f"❌ {err}")

        elif choice == "6":
            try:
                old_pin = int(input("\nEnter current 4-digit PIN: "))
                new_pin = int(input("Enter new 4-digit PIN: "))
                account.change_pin(old_pin, new_pin)
            except ValueError:
                print("❌ PIN must be numbers only.")

        elif choice == "7":
            account.display_transactions()

        elif choice == "8":
            branch_input = input("\nEnter your account branch name to verify: ")
            account.unlock_account(branch_input)

        elif choice == "9":
            print("\n🙏 Thank you for banking with us! Have a wonderful day.\n")
            break

        else:
            print("❌ Invalid option. Please select between 1 and 9.")


if __name__ == "__main__":
    run_bank_system()
