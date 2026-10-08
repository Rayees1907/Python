# count objects using class variables

class Student:

    student_count = 0

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        Student.student_count += 1

    def student_details(self):
        print(f"Name: {self.name}")
        print(f"Roll_No: {self.roll_no}")
        print("-" * 20)

    @classmethod
    def total_Students(cls):
        print(f"Total students are: {cls.student_count}")

stud1 = Student("Rayees", 23)
stud2 = Student("Rayyan", 23)


stud1.student_details()
stud2.student_details()

Student.total_Students()