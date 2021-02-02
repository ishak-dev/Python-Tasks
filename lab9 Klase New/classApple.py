class Apple:
    def __init__(self, price, quantity):
        self.p = price
        self.q = quantity
    def __str__(self):
        return "Price " + str(self.p) + ", Quantity " + str(self.q)
s = Apple(2,5)
print(s)