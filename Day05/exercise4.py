"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla
todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
"""

def is_prime_number(num):
    is_prime = True
    divisible = 0
    counter = 2
    while counter <= num:
        res = num % counter
        # print(f"{num} module {counter} => {res}")
        counter += 1
        if res == 0:
            divisible += 1
        if divisible >= 2:
            is_prime = False
    return is_prime

def count_prime_numbers(num):
    it = 2
    prime_num = list()
    while it <= num:
        if is_prime_number(it):
            prime_num.append(it)
        it += 1
    return prime_num

print(count_prime_numbers(100))
