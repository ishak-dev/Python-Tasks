


def funkcija (str1, str2):   
    x = ""
    br = 0
    for i in range(0, len(str1)):
        br=0
        for j in range (0, len(str2)):            
            if (str1[i] != str2[j]):
                br = br + 1
                if br == len(str2):
                    x = x + str1[i] + " "                                   
    return x      
str1 = input("unesite prvu recenicu ")
str2 = input("unesite drugu recenicu ") 
print("Slova koja nisu ista: ", funkcija(str1, str2))        



        