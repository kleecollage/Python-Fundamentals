import random

options = ["Cara", "Cruz"]
lista_numeros = [1, 2, 3]

def lanzar_moneda():
    return random.choice(options)

def probar_suerte(result, nlist):
    if result == 'Cara':
        print("La lista se autodestruirá")
        return []
    print("La lista fue salvada")
    return lista_numeros

print(probar_suerte(lanzar_moneda(), lista_numeros))