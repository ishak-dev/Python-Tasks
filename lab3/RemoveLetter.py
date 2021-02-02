def function(x,y):
    n = ""
    if (len(x)== 1):
            
            return print("")
    for char in x:
        if char != y:
            n += char
    
    if (len(x) == len(n)):
        print(n[2:])
    else:
        print(n)    



    
x = input("Unesite string: ")
y = input("Unestie slovo: ")
function(x,y)            