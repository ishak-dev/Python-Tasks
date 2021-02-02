class Point:
    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
p = Point(7,6)
print(p)