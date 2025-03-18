name = input("What is your name? ")
sells = float(input("How many sells do you have? "))
commission = round(sells * 0.13, 2)

print(f"{name} sells ${sells}. Commission per month: ${commission}")