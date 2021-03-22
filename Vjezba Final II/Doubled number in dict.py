def function(x):
    for akey in x:
        if x[akey] < 9:
            x[akey] = x[akey] * 2
    return x



x = {"a":2,"b":3,"c":10}
print(function(x))