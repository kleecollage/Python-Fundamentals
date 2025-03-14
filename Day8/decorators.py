def to_upper(text):
    print(text.upper())
def to_lower(text):
    print(text.lower())

my_function = to_upper
my_function("Python")
print(" ======================================== ")

def some_function(function):
    return function
some_function(to_upper("message"))
print(" ======================================== ")

def change_letters(type):
    def to_upper(text):
        print(text.upper())
    def to_lower(text):
        print(text.lower())
    if type == 'upp':
        return to_upper
    elif type == 'low':
        return to_lower
operation = change_letters('upp')
operation('Some nice content')
print(" ======================================== ")

def deco_hi(function):
    def other_fun(word):
        print("Hello")
        function(word)
        print("Bye")
    return other_fun

@deco_hi
def to_upper2(text):
    print(text.upper())
@deco_hi
def to_lower2(text):
    print(text.lower())

to_lower2("PYTHON")
print(" ======================================== ")

def to_upper3(text):
    print(text.upper())
def to_lower3(text):
    print(text.lower())
deco_upper = deco_hi(to_upper3)
to_upper3("klee")
deco_upper("klee")
print(" ======================================== ")










