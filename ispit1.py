def function(x,y):
    bx=0
    by=0
    t = ""
    for i in range(0,len(x)):
            if(x[i] != y):
                t = t + x[i]
                bx+=1
            else:
                by+=1
    if by == 0:
        if(bx==1):
            return ("")
        else:    
            return t[2:]
    if by>0:
        return t    
                        
x = input("Unesite string ")
y = input("Unesite slovo ")
print(function(x,y))