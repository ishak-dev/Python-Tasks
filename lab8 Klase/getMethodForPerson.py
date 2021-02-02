class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def setName (self, newName):
        self.name = newName
    def setAge (self, newAge):
        self.age = newAge

p = person("ishak", 20)
print(p.getName())
print(p.getAge())
p.setName("Melisa")
p.setAge(19)
print(p.getName())
print(p.getAge())