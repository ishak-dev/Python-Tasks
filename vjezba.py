person={"Name": "John", "Age":"6", "Class":"First" }

print (person["Age"])
person["School"] = "DPS"
del person["Class"]
person["Age"] = "8"
print(len(person))
print(list(person.keys()))
print(list(person.values()))
for value in person:
    print(value + " in this dictionary is related to the following value: " + person[value])


print(person)

