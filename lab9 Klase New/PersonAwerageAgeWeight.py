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
    def __str__(self):
        return "Person " + str(self.n) + ", Age " + str(self.a) + ", Weight " + str(self.w)
    def averageAge(self, target):
        nn = self.n + target.n
        avr = int((self.a + target.a))/2
        wrg = int((self.w + target.w))/2
        return Person(nn,avr,wrg)
    
    
o1 = Person("Ishak", 20, 70)
o2 = Person("Kerim", 20, 80)

t = o1.averageAge(o2)

print(t)
print(t.getN())
print(t.getA())

print(t.getW())
