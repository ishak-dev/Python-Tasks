class snake:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname
s = snake("anaconda")
print(s.getName())

s.setName("python")
print(s.getName())