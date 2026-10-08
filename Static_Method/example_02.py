class Employee:

    # CLASS ATTRIBUTES
    company = "ABC"
    employee_count = 0


    # CONSTRUCTOR
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
        Employee.employee_count += 1

    # INSTANCE METHOD
    def employee_details(self):
        print(f"Name: {self.name}")
        print(f"Role : {self.role}")
        print(f"Salary : {self.salary}")
        print(f"Company : {Employee.company}")

    # CLASS METHOD
    @classmethod
    def change_company(cls, comp_name):
        cls.company = comp_name

    @classmethod
    def count_of_employee(cls):
        print(f"Employee Count : {cls.employee_count}")

    # STATIC METHOD
    @staticmethod
    def salary_is_valid(salary):
        if salary > 50000:
            print("valid salary")
        else:
            print("not valid salary")


emp1 = Employee("Rayees", "DevOps Engineer", 2500000)
emp2 = Employee("Rayyan", "Developer", 400000)

emp1.employee_details()
emp2.employee_details()

print(Employee.company)
print(Employee.employee_count)

print(Employee.salary_is_valid(4000000))

