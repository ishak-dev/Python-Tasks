def function(x):
    r = []
    s = ""
    sum1 = 0
    for i in range(1,len(x)):
        if x[i] == "1" or x[i] == "2" or x[i] == "3" or x[i] == "4" or x[i] == "5" or x[i] == "6" or x[i] == "7" or x[i] == "8" or x[i] == "9" :
            s = s + x[i]
        elif x[i-1] == "1" or x[i-1] == "2" or x[i-1] == "3" or x[i-1] == "4" or x[i-1] == "5" or x[i-1] == "6" or x[i-1] == "7" or x[i-1] == "8" or x[i-1] == "9" :
            print(s)
            r.append(s)
            s = ""
    return r





x = "a33a11b33"
print(function(x))