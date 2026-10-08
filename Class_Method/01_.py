# class method

class Employee:

    # class variable
    company = "RK Tech"

    # class method
    @classmethod
    def change_company(cls, company_name):
        cls.company = company_name


emp1 = Employee()
emp2 = Employee()

print(emp1.company)
print(emp2.company)

Employee.change_company("Amazon")

print(emp1.company)
print(emp2.company)