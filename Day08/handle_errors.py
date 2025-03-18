def addition():
    n1 = int(input("enter number: "))
    n2 = int(input("enter number 2: "))
    print(n1 + n2)
    print("addition end ...")

try:
    # Code we want to try
    addition()
except TypeError:
    # Code to exec in case of errors
    print("You are trying to concat incompatible data types")
except ValueError:
    print("That is not a number.")
else:
    # Code to exec in case no errors
    print("Everything OK")
finally:
    # Code to exec either with or without errors
    print("That's all folks")

def ask_number():
    while True:
        try:
            num = int(input("enter number: "))
        except:
            print("That is not a number.")
        else:
            print(f"Your number is {num}")
            break
    print("Exiting...")
ask_number()




