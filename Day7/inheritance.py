class Animal:
    def __init__(self, age, color):
        self.age = age
        self.color = color
    def born(self):
        print("The animal has been born")
    def talk(self):
        print("Animal is talking")

class Bird(Animal):
    def __init__(self, age, color, flight_height):
        super().__init__(age, color) # add inheritance attributes
        # self.age = age
        # self.color = color
        self.flight_height = flight_height
    def talk(self):
        print("Pio pio")
    def fly(self, meters):
        print(f"Animal is flying {meters} m.")


piolin = Bird(2, 'yellow', 60)
piolin.born()
print(piolin.color)
piolin.talk()
piolin.fly(50)

my_animal = Animal(5, "blue")
my_animal.talk()



