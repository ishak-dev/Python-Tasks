def function():
    a = [5,90,13,40]
    suma = 0
    b = [14,50,20,31]
    sumb = 0
    for i in range(0,len(a)):
        if a[i] % 10 == 0:
            suma += a[i]
    for i in range (0,len(b)):
        if b[i]%10 == 0:
            sumb += b[i]
    return suma,sumb,suma+sumb


print(function())