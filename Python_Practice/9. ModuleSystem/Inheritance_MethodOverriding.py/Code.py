class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age) ##
        self.marks = marks
    def display(self):
        #super().display() ##
        print(self.name, self.age, self.marks)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age) ##
        self.salary = salary
    def display(self):
       # super().display() ##
        print(self.name, self.age, self.salary)

s = Student("Alice", 20, 95)
s.display()
e = Employee("Bob", 30, 50000)
e.display() 