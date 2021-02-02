class Person:
    def __init__(self, name):
        self.n = name
    def getN(self):
        return self.n
    def isEmployee(self):
        return False


class Employee(Person):
    def isEmployee(self):
        return True

emp = Person("Geek1")
print(emp.getN(), emp.isEmployee())

emp = Employee("Geek2")
print(emp.getN(), emp.isEmployee())

