class Car:
    name = "Passat"
    k = 200000
    year = 2010
    def ageCar(self):
        ageofcar = 2020-int(self.year)
        return ageofcar
    def kilometers(self):
        if (self.k <= 100000):
            print("great car")
        else:
            print("No")        


c = Car()
print(c.name)
c.ageCar()
print(c.kilometers())  