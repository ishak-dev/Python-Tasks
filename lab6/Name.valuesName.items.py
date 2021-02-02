inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

print(list(inventory.values()))
print(list(inventory.items()))
print("\n")

for (k,v) in inventory.items():
    print("Got", k, "that maps to ",v)

print("\n")

for k in inventory:
    print("Got ", k, "that maps to", inventory[k])