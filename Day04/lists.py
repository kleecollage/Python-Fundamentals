word = 'Python'
my_list = []
for letter in word:
    my_list.append(letter)
print(my_list)

my_list =[letter for letter in my_list]
print(my_list)

my_list =[letter for letter in 'Phyton']
print(my_list)

my_list = [n for n in range(0,21,2)]
print(my_list)

my_list = [n/2 for n in range(0,21,2)]
print(my_list)

my_list = [n for n in range(0,21,2) if n * 2 > 10]
print(my_list)

my_list = [n if n * 2 > 10 else "No" for n in range(0,21,2)]
print(my_list)

feets = [10,20,30,40,50]
meters = [p * 3.281 for p in feets]
print(meters)