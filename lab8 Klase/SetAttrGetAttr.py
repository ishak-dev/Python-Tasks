class cat:
    weight = 15
cat = cat()
setattr(cat, "weight", 10)
value = getattr(cat, "weight")


print(value)