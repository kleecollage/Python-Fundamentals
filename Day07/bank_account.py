"""
person: name, lastname
client(person): no_account, balance
    - method1: Print client (all data client)
    - method2: deposit
    - method3: withdrawal
Program: user deposit, withdrawal or exit
    -functions:
        menu()
        createClient()
"""
from random import randint

class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

class Client(Person):
    def __init__(self, name, lastname, no_account, balance = 0):
        super().__init__(name, lastname)
        self.no_account = no_account
        self.balance = balance
    def __str__(self):
        return f'Name: {self.name} {self.lastname}\nAccount: {self.no_account}\nBalance: ${self.balance}'
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.balance}")
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw: ${amount}. New balance: ${self.balance}")
        else:
            print("Oops. Insufficient funds")
            print(f"Balance: ${self.balance}")

# Show menu options
def menu():
    print("#"*49 + '\n' + '#'*16 + '   BANK SYSTEM   ' + '#'*16 + '\n' + '#'*49)
    options = {
        1: 'Create new client',
        2: 'Withdrawal',
        3: 'Deposit',
        4: 'Exit'
    }
    for o in options:
        print(f'{o}: {options[o]}')
    select = int(input("Select an option: "))
    return select

# Create new client
def new_client():
    name = input("Name: ")
    lastname = input("Lastname: ")
    no_account = randint(0, 1000000)
    x_client = Client(name, lastname, no_account)
    print(x_client)
    return x_client

# Withdrawal fun
def withdrawal():
    amount = int(input("How much amount do you want to withdraw?: "))
    client.withdrawal(amount)

# Deposit fun
def deposit():
    money = int(input("How much money do you want to deposit?: "))
    client.deposit(money)

# START PROGRAM
while (client_selection := menu()) != 4:
    match client_selection:
        case 1: client = new_client()
        case 2: withdrawal()
        case 3: deposit()
        case 4: print('Ciao!')




