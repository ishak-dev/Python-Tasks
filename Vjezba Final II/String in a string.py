def funtion(x,y):
    x = x.split(" ")
    y = y.split(" ")
    r = []
    for char in x:
        if char in y:
            r.append(char)
    r = " ".join(r)
    return r 

x = input("input x: ")
y = input("input y: ")
print(funtion(x,y))
