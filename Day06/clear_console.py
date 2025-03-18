from os import system
from pathlib import Path

ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[3]
print(carpeta)

name = input("Enter your name: ")
age = input("Enter your age: ")

# system('clear')

print(f"Your name is {name} and your age is {age}")

