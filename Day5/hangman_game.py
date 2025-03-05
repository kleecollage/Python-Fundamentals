from random import choice
# GLOBAL VARIABLES
words_list = [
    "apple", "banana", "computer", "dolphin", "elephant",
    "guitar", "happiness", "island", "jungle", "kangaroo",
    "lemon", "mountain", "notebook", "octopus", "penguin"
]
attempts = 5
secret_word = choice(words_list)
secret_word = list(secret_word.strip())
remaining = len(secret_word)
display = ["_"] * len(secret_word)

# USER LETTER CHOICE
def ask_letter():
    return input("Enter a letter: ")

# LETTER CHOICE VALIDATION
def validation(letter):
    is_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while letter.lower() not in is_letter:
        print("Sorry, that's not a letter")
        letter = ask_letter()

# CHECK LETTER IN SECRET WORD
def check_letter(letter):
    global remaining, attempts, display
    print("ENTER TO CHECK LETTER FUN")
    if letter in secret_word:
        print("You lucky bastard!")
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                display[i] = letter
                remaining -= 1
    else:
        attempts -= 1
    print(" ".join(display))
    return secret_word, attempts, remaining

# GAME START
print(" ####################  WELCOME TO HANGMAN GAME  ###############")
while attempts > 0 and remaining > 0:
    print(f"You have {attempts} attempts to guess the secret word.")
    print(" ".join(display))
    user_input = ask_letter()
    validation(user_input)
    check_letter(user_input)
# END GAME
if remaining == 0 and attempts > 0:
    print("Congratulations! You guessed the word:", "".join(secret_word))
else:
    print("You lost! The word was:", "".join(secret_word))


