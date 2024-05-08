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






