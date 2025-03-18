class Parent:
    def talk(self):
        print("Hello")

class Mother:
    def laugh(self):
        print("Ha ha ha")
    def talk(self):
        print("Whats up")

class Son(Parent, Mother):
    pass

class Grandson(Son):
    pass

my_grandson = Grandson()
my_grandson.talk() # priority in order of inheritance
my_grandson.laugh()

print(Grandson.__mro__) # mro = method resolution order


