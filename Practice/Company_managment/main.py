# Class and Instance Variables

class Employee:

    # class variable
    company = "RK Tech"
    employee_count = 0
    
    # init
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
    
        Employee.employee_count += 1
    
    # details of employee
    def employee_info(self):
        print("Name: ", self.name)
        print("Role: ", self.role)
        print("Salary: ", self.salary)
        print("Company: ", Employee.company)
        print("-" * 20)

    
employee1 = Employee("Rahul", "DevOps Engineer", 40000)
employee2 = Employee("Arun", "Python Developer", 45000)
employee3 = Employee("John", "Cloud Engineer", 50000)
employee4 = Employee("Rayees", "DevSecOps Engineer", 200000)

employee1.employee_info()
employee2.employee_info()
employee3.employee_info()

print(Employee.employee_count)