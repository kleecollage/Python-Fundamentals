def check_3_digits(my_list):
    list_3_digits = []
    for n in my_list:
        if n in range(100, 1000):
            list_3_digits.append(n)
        else:
            pass
    return list_3_digits

result = check_3_digits([555, 99, 300])
print(result)


lista_numeros = [1, 2, 3, -1, -2, -3]
def todos_positivos(num_list):
    for num in num_list:
        if num < 0:
            return False
        else:
            pass
    return True



nums = [1, 50, 500, 5000, 750]
def suma_menores(num_list):
    i = 0
    for num in num_list:
        if 0 < num < 1000:
            i += num
    return i
print(suma_menores(nums))

my_nums = [1,2,3,4,5,6,7,8]
def cantidad_pares(list_nums):
    i = 0
    for num in list_nums:
        even = num % 2
        if even == 0:
            i += 1
    return i

print("Even:", cantidad_pares(my_nums))