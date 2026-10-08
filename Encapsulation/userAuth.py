class User:

    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def user_info(self):
        print(f"User_Name: {self.username}")

    def change_pass(self):
        old_pass = input("Enter the old password: ")
        if self.__password == old_pass:
            print("Password matched")
            new_pass = input("Enter the new password: ")
            self.__password = new_pass
            print("Password successfully changed")
        else:
            print("Error while changing password, password not matched")

user_name = input("Enter username: ")
user_pass = input("Enter the password: ")


user1 = User(user_name, user_pass)
user1.user_info()

print("Do u want to change the password ?: ")
confirm_change_pass = input("Enter yes/no: ")

if confirm_change_pass.lower() == "yes":
    user1.change_pass()
else:
    print("Password was not change")
