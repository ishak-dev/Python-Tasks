def function(x):
    br = 0
    for i in range(1,len(x)):
        for j in range(0,len(x[i])):
            if x[i][j][0] == x[i-1][j][0]:
                br +=1
    return br





x = (["aa","bb","cc"],["aaa","b","bb"])

print(function(x))
