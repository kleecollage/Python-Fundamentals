""" Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valor intermedio """

def devolver_distintos(a, b, c):
    res = a + b + c
    if res > 15:
        return max(a,b,c)
    elif res < 10:
        return min(a,b,c)
    elif 10 <= res <= 15:
        num_list = [a,b,c]
        num_list.sort()
        return num_list[1]

print(devolver_distintos(4, 5, 7))