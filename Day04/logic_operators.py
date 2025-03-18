my_bool = 4 < 5 < 6
print(my_bool)

my_bool = 4 < 5 and 5 > 6
print(my_bool)

my_bool = (4 < 5) and (5 == 2 + 3)
print(my_bool)

my_bool = (55 == 55) and ('dog' == 'DOG'.lower())
print(my_bool)

my_bool = (1 == 10) or ( 3 != 30)
print(my_bool)

text = "This is a short phrase"
my_bool = ('phrase' in text) and ('brief' in text)
print(my_bool)

my_bool = not ('a' == 'a')
print(my_bool)

my_bool = not ('a' != 'a')
print(my_bool)