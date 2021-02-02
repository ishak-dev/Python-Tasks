def function(x,y):
    index = x.find(y)
    if index < 0:
        return x
    r = x[:index] + x[index+len(y):]
    return r, index


x = input("Unesite prvi string: ")
y = input("Unesite drugi string: ")
print(function(x,y)) 