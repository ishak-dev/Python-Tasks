def function():
    for i in range(1,100000):
        print(i,"Volim te")
    x = input("Koga voliš? \n ")
    n = 0
    while n == 0:
        if (x != "Melisu"):
            x = input("Probaj ponovo \n")
        else:
            print("Bravo")
            n = 1
    y = input("Koliko je voliš \n")
    r = 0
    while r==0:
        if (y != "Najvise"):
            y = input("Probaj opet ponovo \n")
        else:
            r = 1
    print("Cestitamo prosao si test")



function()
