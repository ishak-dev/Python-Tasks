def function(x):
    b = ""
    c = 0
    summ = 0
    br = 1
    for i in range(1,len(x)+1):
        if(x[-i] >= "a" and x[-i] <="z"):
            c = c+1
            b = b + " "
            br = 1
        else:
            summ = summ + (int(x[-i]) * br)
            br = br * 10
    return summ





x = "aa11e2e2asdsdgdsghb33"
print(function(x))