def my_fun():
    return 4

def my_generator():
    yield 4

print(my_fun())
print(my_generator())
print("========================================")

gen = my_generator()
print(next(gen))
print("========================================")

def my_function():
    my_list = []
    for i in range(1, 5):
        my_list.append(i * 10)
    return my_list

def my_gen():
    for i in range(1, 5):
        yield i * 10

print(my_function())
gen = my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print("========================================")


def generator():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

gen = generator()
print(next(gen))
print(next(gen))
print("Here can go any function or what you want, ")
print("Because Generators save the last state called")
print(next(gen))
print("========================================")

def gen():
    num = 0
    while True:
        num += 1
        yield num

generador = gen()
print(next(generador))
print(next(generador))
print(next(generador))
print("========================================")

def gen():
    num = 7
    i = 1
    while num > 0:
        num = 7 * i
        i += 1
        yield num
generador = gen()
print(next(generador))
print(next(generador))
print(next(generador))
print("========================================")

def gen():
    lives = 3
    while lives > 1:
        yield (f"Te quedan {lives} vidas")
        lives -= 1
    if lives == 1:
        yield (f"Te queda {lives} vida")
    yield("Game Over")
perder_vida = gen()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
