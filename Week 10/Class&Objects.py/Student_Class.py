class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}")
s0 = Student(101, "Alice")
s0.display()
s1 = Student(102, "Bob")
s1.display()
#self is a container which holds the current object
