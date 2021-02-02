class Animal:
    
    
    def speak(self):
        print("Animal is speaking")


class Dog(Animal):
    def bark(self):
        print("Dog barking")



class DogChild(Dog):
    def eat(self):
        print("Eating")

DogChild().speak()
DogChild().bark()
DogChild().eat()

