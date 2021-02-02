inventory = {"aples": 430, "bananas": 312,"oranges": 525, "pears": 217}

for akey in inventory.keys():
    print("Got a key ", akey, "which maps to value", inventory[akey])

print("\n")
ks = list(inventory.keys())
print(ks)
