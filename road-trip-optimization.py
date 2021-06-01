def brojOdmaralista():
    x = int(input("broj odmaralista "))
    while 0 > x or x > 10000000:
        x = input ("Unesite ponovo broj odmaralista")

    y = int(input("broj vozaca "))
    while 0 > y or y > 10000000:
        y = input("Ponovo unesite broj vozaca")
    
    zbirkm = 0
    procent = y/x * 100

    br=0
    km = []
    while br < x:
        brkm = int(input("Unesite broj kilometara "))
        zbirkm = zbirkm + brkm
        km.append(brkm)
        br = br + 1
    z = 0
    for t in km:
        z = z + t
        if ((procent + z) > 90 ):
            z = 0
            break
        else:
            continue
        print ("Vozac je presao ", z)

    return x,y,km,zbirkm
print(brojOdmaralista())
brojOdmaralista()


