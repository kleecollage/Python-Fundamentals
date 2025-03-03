my_list = ['a', 'b', 'c']
for letter in my_list:
    num_letter = my_list.index(letter) + 1
    print(f"Letter {num_letter}:", letter)

names = ['John', 'Jane', 'Michael', 'Samantha', 'Lloyd', 'Gwendolyn']
for name in names:
    if name.startswith('L'):
        print(name)
    else:
        print("No names starting with 'L'")

numbers = [1, 2, 3, 4, 5]
my_val = 0
for number in numbers:
    my_val = my_val + number
print(my_val)

# word = 'Python'
for letter in 'Python':
    print(letter)

for a,b in [[1,2],[3,4],[5,6],[7,8]]:
    print("a",a)
    print("b",b)

dic = {'key1':'a', 'key2':'b', 'key3':'c', 'key4':'d', 'key5':'e'}
for item in dic:
    print(item)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for a,b in dic.items():
    print(a,b)

list_numbers = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
sum_even = 0
sum_odd = 0

for num in list_numbers:
    result = num % 2
    if result == 0:
        sum_even += num
    else:
        sum_odd += num

print(sum_even, sum_odd)



