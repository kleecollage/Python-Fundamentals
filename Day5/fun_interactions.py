from random import shuffle
## STICKS GAME ##
# Init List
sticks = ['-', '--', '---', '----']
# Mix sticks
def mix(flist):
    shuffle(flist)
    return flist
# Ask try
def try_luck():
    attempt = ''
    while attempt not in ['1', '2', '3', '4']:
        attempt = input('Pick a number from 1-4: ')
    return int(attempt)
# Check try
def check_attempt(xlist, attempt):
    if xlist[attempt - 1] == '-':
        print("HaHa. You loose!")
    else:
        print("This time you have been saved!")
    print(f"You took the stick: {xlist[attempt - 1]}")

mixed_sticks = mix(sticks)
selection = try_luck()
check_attempt(mixed_sticks, selection)


## DICES GAME  ##
from random import randint
def lanzar_dados():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2

def evaluar_jugada(d1, d2):
    sum_dices = d1 + d2
    if sum_dices <= 6:
        return f"La suma de tus dados es {sum_dices}. Lamentable"
    elif 6 < sum_dices < 10:
        return f"La suma de tus dados es {sum_dices}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {sum_dices}. Parece una jugada ganadora"

print(evaluar_jugada( *lanzar_dados() ))


## AVERAGE ##
lista_numeros = [1, 2, 15, 7, 2]
def reducir_lista(xlist):
    higher = 0
    for x in xlist:
        if x > higher:
            higher = x
    xlist.remove(higher)
    return list(set(xlist))

def promedio(ylist):
    return sum(ylist) / len(ylist)

print(promedio(reducir_lista(lista_numeros)))