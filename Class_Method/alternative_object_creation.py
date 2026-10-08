# ALTERNATIVE OBJECT CREATION
# CREATION OF OBJECT FROM STRING

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # THIS NAME AND AGE RETURN TO __init__ METHOD =======> Student("Rayees", 23)
    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))          # Student("Rayees", 23)