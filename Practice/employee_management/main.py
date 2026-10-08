class Employee:
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary

    def display_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role: ", self.role)
        print("Salary: ", self.salary)
        print("-" * 20)

    def work(self):
        print(self.name, "is working as a ", self.role, "engineer")
        print("-" * 20)

    def show_salary(self):
        print(self.name, " salary is ", self.salary)
        print("-" * 20)

    def employee_info(self):
        print("Hello, my name is ",self.name)
        print("Iam ",self.age, " years old.")
        print("I work as a ",self.role, " engineer")
        print("My salary is ",self.salary)
        print("-" * 20)

# Create an instance from a class ==== object

employee1 = Employee("Rayees", 24, "DevOps", 250000)
employee1.work()
employee1.show_salary()
employee1.display_details()
employee1.employee_info()


employee2 = Employee("Yunus", 24, "Developer", 120000)
employee2.work()
employee2.show_salary()
employee2.display_details()
employee2.employee_info()