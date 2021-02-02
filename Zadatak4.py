def Digits(n): 
    najveci = 0  
    while (n): 
        r = n % 10  
        najveci = max(r, najveci)   
        n = n // 10
    print(najveci)   
print("unesite broj") 
n = input ()
n = int(n)
Digits(n) 
    
