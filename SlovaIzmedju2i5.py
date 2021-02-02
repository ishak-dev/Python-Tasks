def function(x):
    br = 0
    y = ""
    sr = 0
    for i in range(0,len(x)):
        br=0 
        for j in range(0,len(x)):
            if(x[j] == x[i]):
                br+=1
        sr=0     
        if (br>=2 and br<5):
            for t in range(0,len(y)):
                if(x[i] != y[t]):
                    sr+=1
            
            if(sr == len(y)):
                y = y + x[i] + " "
                     
    return y, br
 
x = input("Unesite recenicu ")
print(function(x))
