person = {"name":"john","age":6,"class":"first"}
print (person["age"])
person["school"] = "DPS"
del person["class"]
person["age"] = 8
len(person)
print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))
print(person.get("name", 0))
for i in person:
    if(i == "name"):
        print("name in this dictionary is related to the following value: ", person[i])
    if(i == "age"):
        print("age in this dictionary is related to the following value: ", person[i])
    if(i == "school"):
        print("school in this dictionary is related to the following value: ", person[i]) 
print("\n")
for r in person:
    print(r, "in this dictionary is related to the following value:", person[r])        
