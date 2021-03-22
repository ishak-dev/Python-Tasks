def function(x):
    y = {}
    r ={}
    for char in x:
        if char != " ":
            if char in y:
                y[char] = y[char] + 1
            else:
                y[char] = 1
    for key in sorted(y.keys()):
        r[key] = y[key]

    return r

x = input()
print(function(x))
        