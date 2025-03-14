from Day8.numbers.generators import gen_pharma, gen_perf, gen_cos


# TURNS GENERATOR
# 3 AREAS:
#   -- Pharmacy
#   -- Perfumery
#   -- Cosmetics
# Every output has to say:
#   -- You turn is
#   -- {TURN}
#   -- Please wait, you will be attended soon
# menu_function() -> ask user to select one of the areas
# selected_area_function() -> returns the next turn
# continue_function() -> asks user if wants to generate another turn

def menu():
    areas = {
        1:"Pharmacy",
        2:"Perfumery",
        3:"Cosmetics",
        # 4:"Exit"
    }
    print("="*78 + "\n" + "="*20 + "   WELCOME TO TURN GENERATOR SYSTEM   " + "="*20 + "\n" + "="*78)
    for op, area in areas.items():
        print(op, area)
    area_selected = int(input("Which area do you want to go to?   "))
    while area_selected not in areas.keys():
        print("Please select a valid area")
        area_selected = int(input("Which area do you want to go to?   "))
    return area_selected

def another_turn():
    options = {
        1:"Yes",
        2:"No",
    }
    print("Would you like to take another turn?")
    for op, value in options.items():
        print(op, value)
    op_select = int(input("Select an option:  "))
    while op_select not in options.keys():
        print("Please select a valid option")
        op_select = int(input("Select an option:  "))
    if op_select == 2:
        exit()
    run_program()

def run_program():
    while True:
        try:
            user_option = menu()
            match user_option:
                case 1:
                    print(next(gen_pharma))
                    another_turn()
                case 2:
                    print(next(gen_perf))
                    another_turn()
                case 3:
                    print(next(gen_cos))
                    another_turn()
            break
        except Exception as e:
            print(f"Error: {e}. Please select a valid area")

run_program()
