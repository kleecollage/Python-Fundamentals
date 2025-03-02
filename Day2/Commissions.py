name = input("What is your name? ")
sells = int(input("How many sells do you have? "))
commission = round(sells * 0.13, 2)
print(f"{name} sells ${sells} commission per month: ${commission}")