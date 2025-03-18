def deco_turn(generator):
    def wrapper():
        gen = generator()
        for turn in gen:
            print("*" * 50)
            yield(
f""" Your turn is:
            {turn}
Please wait, you will be attended soon
**************************************************""")
    return wrapper

@deco_turn
def gen_pharma_turn():
    turn = 0
    while True:
        turn += 1
        yield f"PH-{turn}"

@deco_turn
def gen_perf_turn():
    turn = 0
    while True:
        turn += 1
        yield f"P-{turn}"

@deco_turn
def gen_cos_turn():
    turn = 0
    while True:
        turn += 1
        yield f"C-{turn}"

gen_pharma = gen_pharma_turn()
gen_perf = gen_perf_turn()
gen_cos = gen_cos_turn()

# print(next(gen_pharma))
# print(next(gen_pharma))
# print(next(gen_pharma))