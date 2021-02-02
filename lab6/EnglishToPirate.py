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

change = []
num = x.split()
for aword in num:
    if aword in words:
        change.append(words[aword])
    else:
        change.append(aword)
print(" ".join(change))            
        
