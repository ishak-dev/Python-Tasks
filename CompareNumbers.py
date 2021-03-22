def evenlySpaced(a,b,c):
    if(a>b>c):
        if (a-b == c):
            return True
        else:
            return False      
    if(b>c>a):
        if (b-c == a):
            return True
        else:
            return False      
    if(c>a>b):
        if (c-a == b):
            return True 
        else:
            return False      
    if(b>a>c):
        if (b-a == c):
            return True
        else:
            return False       
    if(a>c>b):
        if (a-c == b):
            return True
        else:
            return False      
    if(c>b>a):
        if (c-b == a):
            return True
        else:
            return False                                             
        








a = int(input("unesite prvi broj: "))
b = int(input("unesite drugi broj: "))
c = int(input("unesite treci broj: "))
print(evenlySpaced(a,b,c))
