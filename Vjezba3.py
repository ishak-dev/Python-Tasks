def function(x):
    r = ""
    for akey in x:
        r = ""
        r = str(x[akey])
        x[akey] = r[-1]
    return x

x = {"a":29}
print(function(x))