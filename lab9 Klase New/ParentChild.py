class Person:
    def __init__(self, firstname, lastname):
        self.f = firstname
        self.l = lastname
    def printname(self):
        print(self.f, self.l)
x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self, firstname,lastname, year):
        #Person.__init__(self, firstname,lastname)
        super().__init__(firstname,lastname)
        self.g = year

    def welcome(self):
        print("Welcome " + self.f + self.l + "to the class of ", self.g)
    
x = Student("Mike", "Olsen", 2019)
x.welcome()
