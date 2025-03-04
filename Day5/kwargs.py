def test(num1, num2, *args,**kwargs):
    print(f"First value is: {num1}")
    print(f"Second value is: {num2}")

    for arg in args:
        print(f"Arg = {arg}")

    for key,value in kwargs.items():
        print(f"{key} = {value}")


test(15, 50, 1,2,3,4,5, x='one', y='two', z='tree')

args = [100,200,300,400]
kwargs = {'x':'apple', 'y':'orange', 'z':'pineapple'}
test(20, 50, *args, **kwargs)

def cantidad_atributos(**kwargs):
    return len(kwargs)
print(cantidad_atributos(x='apple', y='orange'))

def lista_atributos(**kwargs):
    return list(kwargs.values())
print(lista_atributos(x='apple', y='orange'))


def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print(describir_persona("John", color_ojos="azules", color_pelo="rubio"))