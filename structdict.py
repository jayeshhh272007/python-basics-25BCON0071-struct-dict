
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student = Student("Jayesh", 19, "BTech CSE")

student_dict = student.__dict__

print(student_dict)
