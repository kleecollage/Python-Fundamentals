my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
index = 0

for item in my_list:
    print(index, item)
    index += 1

# ENUM method
for index, item in enumerate(my_list):
    print(index, item)

for item in enumerate(my_list):
    print(item)

for index, item in enumerate(range(50, 55)):
    print(index, item)

my_list = list(enumerate(my_list)) #tuples
print(my_list)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for idx, name in enumerate(lista_nombres):
    if name[0] == 'M':
        print(idx)