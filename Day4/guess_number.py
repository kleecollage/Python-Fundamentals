from random import *

print("###########   GUESS THE NUMBER   ###########")
print("I'm thinking a number between 0 and 99")
attempts = 0
answer = randint(0, 100)
while attempts < 3:
    u_answer = input("Try your best shot: ")
    attempts += 1

    try:
        u_answer = int(u_answer)
    except ValueError:
        print("Hey, you didn't enter a valid number!")
        continue

    if u_answer < answer:
        print("Too low")
    elif u_answer > answer:
        print("Too high")
    else:
        print("You got it right!, the answer is", answer)

    if attempts == 3:
        print("Sorry, the answer was", answer)
        break