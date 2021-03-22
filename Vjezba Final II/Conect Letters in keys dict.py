def function(x):
    for i in list(x):
        if " " in i:

            r = i.replace(" ", "")
            x[r] = x.pop(i)
            
    return x



x = {"b r":1,"ss":2}
print(function(x))