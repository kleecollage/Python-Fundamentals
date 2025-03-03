var1 = True
var2 = False
print(type(var1))
print(var1) #true

number = 5 > 2+3
print(number) # false
number = 5 < 2+3
print(number) # false
number = 5 == 2+3
print(number) # true
number = 5 >= 2+3
print(number) # true
number = 5 <= 2+3
print(number) # true

number = bool(5<6)
print(number) # true

number = bool()
print(type(number))
print(number) # false (default)

my_list = [1,2,3,4]
control = 5 in my_list
print(type(control))
print(control) # false
control = 5 not in my_list
print(control) # true

print(25**(1/2) == 5)