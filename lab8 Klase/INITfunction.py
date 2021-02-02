class person:
    name = ""
    age=0
    def __init__(self, name, age):
        self.name = name
        self.age = age



p = person("melisa", 25)
print(p.name)
print(p.age)

