def my_sum(*args):
    return sum(args)
print(my_sum(1,2,3,4,5,6))


def suma_absolutos(*args):
    suma = 0
    for arg in args:
        if arg < 0:
            arg = arg * -1
        suma += arg
    return suma
suma_absolutos(-1,-2,-3,4,5,6)

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return print(f"{nombre}, la suma de tus números es {suma_numeros}")

numeros_persona("Federico", 75, 20, 65)