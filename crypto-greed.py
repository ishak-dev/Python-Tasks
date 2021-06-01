n = int(input("Unesite vrijednost koje mali Muamer posjeduje "))
k = int(input("Unesite broj planeta na kojima su vanzemaljci "))
br = 0
zarada = 0
prodaja = 0
listgroup = []
group = []
IFbreak = False
while k > 1000:
    k = int(input("molimo vas unesite ponovo broj planeta "))
while br <= k-1:
    b = input("Unesite cijene po planeti ")
    group = b.split()
    listgroup.append(group)
    br = br + 1
print(listgroup)

for i in range (0,len(listgroup)):
    for j in range(0,(len(listgroup[i]))):
        
        for num in listgroup[i][j]:
           
                 
                r = int(listgroup[i].index(num))
            
                if (r != 0):
                    
                    if (int(num) >= int(listgroup[i][(j-1)])):
                    
                        zarada = zarada + int(num)
                        prodaja = prodaja + 1
                        print(prodaja)
                    else:
                        prodaja = 0
                        break
                        
                        
                else:
                    prodaja = 0
                
                
    print(prodaja)

        
         




    
