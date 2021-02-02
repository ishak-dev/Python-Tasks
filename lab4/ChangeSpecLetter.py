def function(a,b,c):
    r = ""
    for char in a:
        if char == b:
            char = c
            r+=char
        else:
            r+=char    
    return r        


a = input("Unesite prvu recenicu: ")
b = input("Unesite slovo koje zelite zamjenit: ")
c = input("Unesite zamjensko slovo: ")
print(function(a,b,c))