import math
def function(x):
    sr = math.sqrt(x)
    return ((sr - int(sr)) == 0)


x = 16
if (function(x)):
    print("Yes")
else:
    print("No")        