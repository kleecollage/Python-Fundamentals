my_list = ["a", "b", "c"]
print(type(my_list))

result = len(my_list)
print(result)

print(my_list[0:2])

other_list = ["hello", 55, 3.14]
print(other_list)

my_list2 = ["d", "e", "f"]
print(my_list + my_list2)
print(my_list + other_list)

my_list3 = my_list + my_list2
print(my_list3)

my_list3[0] = "alfa"
print(my_list3)

my_list3.append("g")
print(my_list3)

deleted = my_list3.pop(0)
print(my_list3)
print(deleted)

my_list4 = ['g', 'o', 'm', 'c', 'a', 'z']
my_list4.sort()
print(my_list4)

my_list4.reverse()
print(my_list4)

