class Bird:
    wings = True
    def __init__(self, parameter, my_color):
        self.attribute = parameter
        self.color = my_color

    def pio(self):
        print("Pio Pio, my color is {}".format(self.color))

    def volar(self, meters):
        print(f"The bird has fly {meters} meters")
        self.pio()

    def paint_black(self):
        self.color = "black"
        print("Now im black ewe")

    @classmethod
    def put_eggs(cls, quantity):
        print(f"I laid {quantity} eggs")
        cls.wings = False
        print(Bird.wings)
        # print(f"Im color {self.color}") # Not supported

    @staticmethod
    def look():
        print("I am looking")
        # self.color = "red" # not supported
        # cls.wings = False # not supported

Bird.put_eggs(3)
Bird.look()

piolin = Bird('canary','yellow')
piolin.pio()
piolin.volar(100)
piolin.paint_black()
piolin.wings = False
print(piolin.wings)



my_bird = Bird('tucan', 'red')
print(my_bird)
print(type(my_bird))
print(my_bird.attribute)

other_bird = Bird('bat', 'blue')
print(other_bird)
print(type(other_bird))

print(my_bird.wings)
print(Bird.wings)

