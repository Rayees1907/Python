# Instance Method

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    # this is instance method bez it works with the data of a particular object
    def display(self):
        print("Name: ", self.name)
        print("Salary: " , self.salary)

    
employee1 = Employee("Rayees", 2700000)
employee2 = Employee("Rayyan", 2300000)

employee1.display()
employee2.display()