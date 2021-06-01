import math
class Point:
    def __init__ (self, vrjX, vrjY):
        self.x = vrjX
        self.y = vrjY
        
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distancaOrigin(self):
        origin = ((self.x **2) + (self.y **2))** 0.5    
        return origin
    
def distanca (Point1, Point2):
    
    xdif = Point2.getX() - Point1.getX()
    ydif = Point2.getY() - Point1.getY()
    distanca = math.sqrt(xdif**2 + ydif**2)
    
    return distanca



p = Point(4,3)
q = Point(0,0)
print(distanca(p,q))
