user_text = input("Write something or you're gay: ")
user_letter = input("Which letter would you like to count how many times is repeated? ")
user_text.lower()

print(f"The total times '{user_letter}' is repeated are:  {user_text.count(user_letter)}")

list_words = user_text.split()
print(f"In total, your text has: {len(list_words)} words")

print(f"The first letter on the text is: '{user_text[0]}'. And the last one is: {user_text[-1]} ")

list_words.reverse()
reversed_text = '-'.join(list_words)
print("Your texts backwards says:", ' '.join(reversed_text))

python_exists = 'python' in user_text
dic = {True:"DOES", False:"DOES NOT"}
print(f"The word 'python' {dic[python_exists]} appears on your text")
