dictionary = {'c1':'value1', 'c2':'value2'}
print(dictionary)

result = dictionary['c1']
print(result)

client = {'name':'John', 'lastname':'Doe', 'weight':62, 'height':4.6}
query = (client['height'])
print(query)

dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

dic2 = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}
print((dic2['c2'][1]).upper())

dic3 = {1:'a', 2:'b'}
print(dic3)
dic3[3] = 'c'
print(dic3)
dic3[2] = 'B'
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['edad'] = 36
print(mi_dic)


