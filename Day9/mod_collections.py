from collections import Counter, defaultdict, namedtuple, deque

numbers = [ 8,6,2,4,4,7,8,5,1,2,3,6,5,4,8,9,5,4,1,2,4 ]
print(Counter(numbers))
print("-" * 25)

print(Counter('mississippi'))
print("-" * 25)

phrase = 'al pan pan y al vino vino'
print(Counter(phrase.split()))
print("-" * 25)

series = Counter([1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,4])
print(series.most_common(2))
print(list(series))
print("-" * 25)

my_dic = defaultdict(lambda: 'nothing')
my_dic['one'] = 'green'
print(my_dic['two'])
print(my_dic)
print("-" * 25)

Person = namedtuple('Person', ['name', 'age', 'weight'])
john = Person('John', '25', 80)
print(john.weight)
print(john[2])
print("-" * 25)


cities = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
cities.appendleft("Ámsterdam")
cities.appendleft("Bruselas")