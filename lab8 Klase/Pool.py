class pool:
    def __init__(self, length, width, depth, temp):
        self.length = length
        self.width = width
        self.depth = depth
        self.temp = temp
    def getLength(self):
        return self.length
    def getWidth(self):
        return self.width
    def getDepth(self):
        return self.depth
    def getTemp(self):
        return self.temp

    def setLength(self, newLength):
        self.length = newLength
    def setWidth(self, newWidth):
        self.width = newWidth
    def setDepth(self, newDepth):
        self.depth = newDepth
    def setTemp(self, newTemp):
        self.temp = newTemp
    
    def calArea(self):
        a = self.length * self.width
        return a
    def calVol(self):
        v = self.length * self.width * self.depth
        return v
    def olymp(self):
        if (self.length == 50 and self.width == 25 and self.depth >= 2):
            if(self.temp >= 25 and self.temp <= 28):
                return True
            else:
                return False
        else:
            return False
    

l = int(input("Unesite L"))
w = int(input("Unesite W"))
d = int(input("Unesite D"))
t = int(input("Unesite T"))
p = pool(1, 2, 3, 4)
p.setLength(l)
p.setWidth(w)
p.setDepth(d)
p.setTemp(t)
print(p.getLength())
print(p.getWidth())
print(p.getDepth())
print(p.getTemp())
print(p.calArea())
print(p.calVol())
print(p.olymp())




