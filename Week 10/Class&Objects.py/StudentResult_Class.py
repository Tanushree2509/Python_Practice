class Student:
    def __init__(self,roll_no,name,total):
        self.roll_no = roll_no
        self.name = name
        self.total = total
    def display(self):
        print(self.roll_no, self.name, self.total)
    def result (self):
        if self.total >= 100:
            print("Pass")
        else:
            print("Fail")
s0 = Student(101,"Alice", 150)
s0.display()
s0.result()
s1 = Student(102,"Bob", 90)
s1.display()
s1.result()