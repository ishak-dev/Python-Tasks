class point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
        


class rectangle():
    def __init__(self,point, height, width):
        self.point = point
        self.h = height
        self.w = width
    def getPoint(self):
        return self.point
    def getH(self):
        return self.h
    def getW(self):
        return self.w
    def setH(self,height):
        self.h = height
    def setW(self,width):
        self.w = width
    def __str__(self):
        return ("Width: ") + str(self.w) + ",Height is: " + str(self.h)
    def transposeWH(self):
        trs = self.w
        self.w = self.h
        self.h = trs
    def isPointRectangle(self, point):
        x2 = self.point.x + self.w
        y2 = self.point.y + self.h
        if (self.point.getX() >= self.point.x and point.getX() <=x2):
            if (point.getY()>self.point.y and point.getY() <= y2):
                return True
        return False


    
r = rectangle(point(1, 1), 2, 4)
print(r.getPoint().getY())
print(r.__str__())
r.transposeWH()
print(r.__str__())
print(r.isPointRectangle(point(1,2)))