
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class rectangle:
    def __init__(self,point,width,height):
        self.p = point
        self.w = width
        self.h = height
    def getPoint(self):
        return self.p
    def getHeight(self):
        return self.h
    def getWidth(self):
        return self.w
    def setPoint(self,point):
        self.p = point
    def setWidth(self,width):
        self.w = width
    def setHeight(self,height):
        self.h = height
    def __str__(self):
        return "Height: " + str(self.h) + "Width: " + str(self.w)
    def isPoint(self, point):
        x2 = self.p.x + self.w
        y2 = self.p.y + self.h
        print((x2 + self.p.x)/2)
        print((y2 + self.p.y)/2)
        print(self.w)
        print(self.h)
        
        if ((point.getX() == self.p.x and point.getY() == self.p.y) or (point.getX() == x2 and point.getY() == self.p.y) or (point.getX() == self.p.x and point.getY() == y2) or (point.getX() == x2 and point.getY() == y2)):
            return True
        elif(point.getX() == (x2 + self.p.x)/2 and point.getY() == (y2 + self.p.y)/2):
            return True
        else:
            return False
    def isDiagonale(self,point):
        x2 = self.p.x + self.w
        y2 = self.p.y + self.h

        if()
    
        
        



r = rectangle(point(1,2),2,3)
c = point(1,5)
print(r.isPoint(point(2,3)))
