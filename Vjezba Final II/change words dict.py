def function(x):
    y = {}
    y["sir"] = "matey"
    y["hotel"]= "fleabag inn"
    y["boy"]= "matey"
    y["restroom"]= "head"

    r = x.split()

    for akey in y:
        for i in range(0,len(r)):
            if akey == r[i]:
                r[i] = y[akey]
    x = " ".join(r)

    return x



x = input()
print(function(x))