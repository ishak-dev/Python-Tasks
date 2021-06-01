x = input("Input sentencese: ")
x = x.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter = {}
for char in x:
    if char in alphabet:
        if char in letter:
            letter[char] = letter[char] + 1
        else:
            letter[char] = 1
print (letter)
keys = letter.keys()
for char in sorted(keys):
    print(char, letter[char])