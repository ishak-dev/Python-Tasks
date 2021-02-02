def function(x):
    if (x == 1):
        return 1
    if (x == 2):
        return 2
    if (x == 3):
        return 3
    if (x == 4):
        return 4            
y = True
while y == True:
    x = int(input("unesi broj menija: "))
    if x == 5:
        print("Odabrali ste Exit")
        y = False
        break
    else:
        print("Odabrali ste Meni broj: ",function(x))    

