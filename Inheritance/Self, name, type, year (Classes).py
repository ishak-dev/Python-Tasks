class pet:
    def __init__(self, name, typee, year):
        self.n = name
        self.t = typee
        self.y = year
    def getN(self):
        return self.n
    def getT(self):
        return self.t
    def getY(self):
        return self.y
    def setN(self, name):
        self.n = name
    def setT(self, typee):
        self.t = typee
    def setY(self, year):
        self.y = year
    def calculate(self):
        zbir = 2021 - int(self.y)
        return zbir

name  = input("Unesite ime ")
typee = input( "Unesite vrstu ")
year = input("Unesite godinu rodjenja ")
p = pet(name, typee, year)
print(p.getN(), p.getT(), p.getY(), p.calculate())


