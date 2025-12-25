# Study of Object Oriented Programming Concepts

# Class and Object
class Student:
    def __init__(self, name, roll_no, dept):
        self.name = name
        self.roll_no = roll_no
        self.dept = dept

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Department:", self.dept)

# Inheritance
class Result(Student):
    def __init__(self, name, roll_no, dept, marks):
        super().__init__(name, roll_no, dept)
        self.marks = marks

    def show_result(self):
        self.display()
        print("Marks:", self.marks)

# Object creation
student1 = Result("Kavi", 101, "CSE", 85)
student1.show_result()
