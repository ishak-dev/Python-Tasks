def encrypt(x,y):
    alphabet = "badcfeghjilknmporqtsvuxwzy"
    e = ""
    for char in x:
        if char == " ":
            e = e + " "
        else:
            pos = alphabet.find(char)
            e = e + cip[pos] 
    return e
cip = "abcdefghijklmnopqrstuvwxyz"
e = encrypt('hfkkp xpqkc', cip)
print(e)
