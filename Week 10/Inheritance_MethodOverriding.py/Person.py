class Person:
    def __init__(self, name, age):
        self.name = name
        '''This is Public Member'''
        self.age = age 
        # self.__age = age (Private Members) 
        #so that it can't be accessed outside the class

    def display(self):
        print(self.name, self.age)