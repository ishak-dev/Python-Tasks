d = {"apples": 15, "bananas": 35, "grapes": 12}
d["bananas"]
d["oranges"]=20
len(d)
"grapes" in d
d["pears"]
d.get("pears", 0)
fruits = d.keys()
fruits.sort()
print(fruits)
del d["apples"]
"apples" in d