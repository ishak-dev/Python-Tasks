def function():
    n = input("input string: ")
    d = True   
    while d == True:
        a = input("input a letter that you want to remove: ")
        l = len(n)
        b = len(n)
        for i in range(0, l):       
            if (n[i] == a):
                n = n.replace(n[i],"")                
                break
            else:
                continue                             
        if b == len(n):
            n = n.replace(n[0],"")
            b = len(n)            
        print(n)             
function()            
                
        
