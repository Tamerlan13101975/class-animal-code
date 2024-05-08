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


    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное{animal}добавлено в зоопарк")



    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"Сотрудник{new_staff}добавлено в зоопарк")

