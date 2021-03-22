def function(x,y):
    max1 = 0
    max2 = 0
    for i in x:
        if i % 10 == 0:
            if i > max1:
                max1 = i
    for j in y:
        if j % 10 == 0:
            if j > max2:
                max2 = j
    
    return max1+max2

x = [1,2,50]
y = [1,2,10]
print(function(x,y))

