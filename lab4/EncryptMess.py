def encrypt(x,y):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    e = ""
    for char in x:
        if char == " ":
            e = e + " "
        else:
            pos = alphabet.find(char)
            e = e + cip[pos] 
    return e
cip = "badcfeghjilknmporqtsvuxwzy"
e = encrypt('hello world', cip)
print(e)
