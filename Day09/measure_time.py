import time

def test_for(number):
    my_list = []
    for num in range(1, number + 1):
        my_list.append(num)
    return my_list

def test_while(number):
    my_list = []
    counter = 1
    while counter <= number:
        my_list.append(counter)
        counter += 1
    return my_list

print(test_for(5))
print(test_while(5))

start = time.time()
test_for(100000)
end = time.time()
print(end - start)

start = time.time()
test_while(100000)
end = time.time()
print(end - start)



import timeit

statement = """
test_for(10)
"""

my_setup = """
def test_for(number):
    my_list = []
    for num in range(1, number + 1):
        my_list.append(num)
    return my_list
"""

duration = timeit.timeit(statement, my_setup, number=1000000)
print(duration)



statement = """
test_while(10)
"""

my_setup = """
def test_while(number):
    my_list = []
    counter = 1
    while counter <= number:
        my_list.append(counter)
        counter += 1
    return my_list
"""

duration = timeit.timeit(statement, my_setup, number=1000000)
print(duration)
