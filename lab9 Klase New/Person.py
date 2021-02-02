class Person:
    def __init__(self, name, age, weight):
        self.n = name
        self.a = age
        self.w = weight
    def getN(self):
        return self.n
    def getA(self):
        return self.a
    def getW(self):
        return self.w
    def setN(self, name):
        self.n = name
    def setA(self, age):
        self.a = age
    def setW(self, weight):
        self.w = weight
    #Convert Person object to a String
    def __str__(self):
        return "Name: " + str(self.n) + ", age: " + str(self.a) + ", Weight: " + str(self.w)
    
    

def olderPerson(Person1, Person2):
    if int(Person1.getA()) > int(Person2.getA()):
        print(Person1.getN() + " is older")
    else:
        print(Person2.getN() + " is older")
def sumWeight(Person1, Person2):
    suma = Person1.getW() + Person2.getW()
    return suma


osoba1 = Person("Ishak", 23, 70)
osoba2 = Person("Kerim", 24, 90)
print(olderPerson(osoba1, osoba2))
print(sumWeight(osoba1, osoba2))
print(osoba1)
print(osoba2)