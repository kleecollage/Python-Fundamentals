minor = min(58, 65, 26, -6, 0, -36)
major = max(58, 65, 26, -6, 0, -36)
print(minor, major)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(my_list), max(my_list))
print(f"Minor is: {min(my_list)}\nMajor is: {max(my_list)}")

names = ['John', 'Jane', 'Alice', 'Emily', 'Michael', 'Zelt']
print(min(names), max(names))

name = "Jane"
print(min(name).lower(), max(name).lower())

dic = {'C1':45, 'C2':11}
print(min(dic), max(dic))
print(min(dic.values()), max(dic.values()))