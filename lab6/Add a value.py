released = {
    "iphone": 2007,
    "iphone 3G": 2008,
    "iphone 3GS": 2009,
    "iphone 4": 2010,
    "iphone 4S": 2011,
    "iphone 5": 2012
    }


released["iphone 5S"] = 2013
print (released)
del released["iphone"]
print (released)
released["iphone 4S"] = 0
print (released)
print (len(released))
released.clear() 
print (released)