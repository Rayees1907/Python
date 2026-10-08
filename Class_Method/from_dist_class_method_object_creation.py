# CREATION OF OBJECT FROM DICTIONARY
# This is useful when working with JSON/API data, because JSON data is commonly converted into Python dictionaries.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dist(cls, data):
        return cls(
            data["name"],
            data["age"]
        )

    def student_details(self):
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")


data1 = {
    "name" : "Rayees",
    "age" : 24
}

data2 = {
    "name" : "Rayyan",
    "age" : 23
}

stud1 = Student.from_dist(data1)
stud1.student_details()

stud2 = Student.from_dist(data2)
stud2.student_details()