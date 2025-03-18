names = ['John', 'Jane', 'Michael', 'Jerry', 'Vincent', 'Isabella', 'Samantha']
ages = [15, 50, 69, 15, 47, 32, 27, 11]
cities = ['Beijing', 'Shanghai', 'Singapore', 'Tokyo']
combined = list(zip(names, ages, cities))

print(combined)

for name, age, city in combined:
    print(f"{name} has {age} years old and lives in {city}")