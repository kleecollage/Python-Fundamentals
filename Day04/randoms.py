from random import *

random_num = randint(1, 50)
print(random_num)

random_num = round(uniform(1, 5),5)
print(random_num)

random_num = random()
print(random_num)

colors = ['blue', 'red', 'purple', 'yellow']
random_item = choice(colors)
print(random_item)

numbers = list(range(5,50,5))
print(numbers)
shuffle(numbers)
print(numbers)
