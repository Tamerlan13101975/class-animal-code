class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} кушает")

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("чирик чирик")


class Mammal(Animal):
    def make_sound(self):
        print("гав гав")


class Reptile(Animal):
    def make_sound(self):
        print("шсшсшсшш")


    def animal_sound(animals):
        for animal in animals:
            animal.make_sound()


class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []
        


