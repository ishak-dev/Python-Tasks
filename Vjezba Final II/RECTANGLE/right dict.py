def function(x):
    y = []
    br = 0
    for i in range(0,len(x)):
        if "z" in x[i]:
            br = 0
        else:
            y.append(x[i])
    return y




x = ["aaa","bbzb","aza"]
print(function(x))