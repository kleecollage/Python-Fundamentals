# Sintaxis
my_set = set([1,2,3,4,5])
my_set = set({1,2,3,4,5})
my_set = set((1,2,3,4,5))
print(type(my_set))
print(my_set)

other_set = {1,2,3,'a','b','c'}
print(type(other_set))
print(other_set)

# print(my_set[0]) # No order collections
# my_set[0] = 5 # Not indexable

my_set = set({1,2,3,4,5,5,4,3,2,1,2,3,4,5}) # Unique elements
print(my_set)

# my_set = set({1,2, [1, 2], 3,4,5}) # Sets are immutables, therefore, Lists are not supported
my_set = set({1,2, (1, 2, 3), 3,4,5}) # Tuples admitted (immutables)
print(my_set)

# Methods
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)

s1.remove(2)
print(s1)

s1.discard(6)
print(s1)

s1.pop()
print(s1)

s1.clear()
print(s1)