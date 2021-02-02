def function(x,y):
    c = ""
    br=0
    for char in x:
        if (char == y):
            br+=1
        else:
            print(char, end="")    

    


x = input("Unesite recenicu: ")
y = input("Unesite slovo: ")
function(x,y) 