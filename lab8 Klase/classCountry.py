class country:
    def __init__(self, name, capitalcity, population):
        self.name = name
        self.capitalcity = capitalcity
        self.population = population

    def getName(self):
        return self.name
    def getCapitalcity(self):
        return self.capitalcity
    def getPopulation(self):
        return self.population

    def setName(self, newName):
        self.name = newName
    def setCapitalcity(self, newCapitalcity):
        self.capitalcity = newCapitalcity
    def setPopulation(self, newPopulation):
        self.population = newPopulation
    
c = country("Bosna", "Sarajevo", 400000)
print(c.getName())
print(c.getCapitalcity())
print(c.getPopulation())
c.setName("Njemacka")
c.setCapitalcity("Berlin")
c.setPopulation(1000000)
print(c.getName())
print(c.getCapitalcity())
print(c.getPopulation())

        