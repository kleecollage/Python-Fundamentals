class Cow:
    def __init__(self, nombre):
        self.nombre = nombre
    def talk(self):
        print(self.nombre + " says Mooouuuwu")

class Ship:
    def __init__(self, nombre):
        self.nombre = nombre
    def talk(self):
        print(self.nombre + " says Bee-ee bee-e ewe")

cow1 = Cow("Aurora")
ship1 = Ship("Cloudy")

cow1.talk()
ship1.talk()

animals = [cow1, ship1]
for animal in animals:
    print("Polymorphism")
    animal.talk()

def animal_talk(animal):
    animal.talk()

animal_talk(cow1)
animal_talk(ship1)

