from random import shuffle

# Init List
sticks = ['-', '--', '---', '----']
# Mix sticks
def mix(flist):
    shuffle(flist)
    return flist
# Ask try
def try_luck():
    attempt = ''
    while attempt not in ['1', '2', '3', '4']:
        attempt = input('Pick a number from 1-4: ')
    return int(attempt)
# Check try
def check_attempt(xlist, attempt):
    if xlist[attempt - 1] == '-':
        print("HaHa. You loose!")
    else:
        print("This time you have been saved!")
    print(f"You took the stick: {xlist[attempt - 1]}")

mixed_sticks = mix(sticks)
selection = try_luck()
check_attempt(mixed_sticks, selection)