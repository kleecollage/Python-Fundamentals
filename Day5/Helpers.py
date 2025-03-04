dic = {'Key1':100, 'Key2':500}

a = dic.popitem()
print(a)
print(dic)

text = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
text = text.lstrip(",:%_#")
print(text)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
print(conjuntos_aislados)

