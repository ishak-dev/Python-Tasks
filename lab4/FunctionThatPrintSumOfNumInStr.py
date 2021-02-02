def function():
    s = "l0e3ve123"
    c = 0
    br = 0

    for i in range(len(s)):
        if s[i] >="0"and s[i] <="9":
            c = c + int(s[i])
            br = br + 1
    print(c, br)        
    



function() 