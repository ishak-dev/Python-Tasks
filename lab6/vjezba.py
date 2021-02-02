x = input("Unesite recenicu ")

words = {
    "sir": "pirate",
    "hotel": "matey",
    "student": "swabbie",
    "boy": "matey",
    "madam": "proud beauty",
    "progessor": "foul blaggart",
    "restaurant": "galley"
}

newwords = []
splitwords = x.split()
for char in splitwords:
    if char in words:
        newwords.append(words[char])
    else:
        newwords.append(char)
print(" ".join(newwords))            
