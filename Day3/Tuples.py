my_tuple = (1, 2, 3, 4)
# my_tuple[0] = 5 # Assignation not supported
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-2])

my_tuple = (1, 2, (10, 20), 3, 4)
print(my_tuple[2][0])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple = tuple(my_tuple)
print(type(my_tuple))

t = (1,2,3,1)
w, x, y, z = t
print(x, y, z)

print(t.count(1))
print(t.index(2))

