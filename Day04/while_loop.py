coins = 5
while coins > 0:
    print(f"I have {coins} coins: ")
    coins -= 1
else:
    print("No coins left")

response = 'y'
while response == 'y':
    response = input("Do you want to continue? [Y/N]: ")
else:
    print("Thank you for playing")

while response == 'y':
    pass
print("Goodbye")

name = input("What is your name? ")
for letter in name:
    if letter == 'a':
        break
    print(letter)

name = input("What is your name? ")
for letter in name:
    if letter == 'a':
        continue
    print(letter)

