"""
✓1. Welcome message
✓2. Indicate the location of the recipes
✓3. Show how many recipes we have in each directory
✓4. Menu options
    ✓- Read recipe
        ✓I. Choose category
        ✓II. Show recipes
        ✓III. Choose recipe
        ✓IV. Read recipe
    ✓- Create recipe
        ✓I. Choose Category
        ✓II. Create Name
        ✓III. Create content
    ✓- Create category
        ✓I. Category Name
        ✓II. Create Category
    ✓- Delete recipe
        ✓I. Choose category
        ✓II. Show recipes
        ✓III. Choose recipe
        ✓IV. Remove recipe
    ✓- Delete category
        ✓I. Choose category
        ✓II. Remove category
    ✓- End Program
"""
import os
import shutil
from pathlib import Path

dir_path = os.getcwd()
recipes_location = Path(dir_path) / "Recetas"
guide = Path(recipes_location)
sub_dirs = [dirs for dirs in recipes_location.iterdir() if dirs.is_dir()]

# Categories
def get_category_recipe():
    total_recipes = 0
    for sub_dir in sub_dirs:
        recipes = list(sub_dir.glob("*.txt"))
        recipes_category = len(recipes)
        print(f"{sub_dir.name}: {recipes_category} recipes")
        total_recipes += recipes_category
    recipes = list(Path(guide).glob("**/*.txt"))
    total_recipes = len(recipes)
    print("Total:", total_recipes)

# User choice
def ask_user_text():
   return input(">>> ")

def ask_user():
    return int(input(">>> "))

# Validate option
def validate_option(user_input, options):
    while True:
        if user_input in options:
            return user_input
        elif user_input not in options:
            print("Sorry, that option is not valid. Please try again.")
            user_input = ask_user()

# Show recipes
def show_recipes(category):
    recipes = list(category.glob("*.txt"))
    options = []
    print("\n..:: Recipes ::..")
    for j, recipe in enumerate(recipes, start=1):
        options.append(j)
        print(f"{j}: {recipe.stem}")
    user_input = ask_user()
    validate_recipe = validate_option(user_input, options)
    selected_recipe = recipes[int(validate_recipe) - 1]
    print(f"\nReading recipe:\n {selected_recipe.stem}")
    with open(selected_recipe, "r") as file:
        print(file.read())
    show_menu()

# Show categories
def show_categories():
    print("Choose the category")
    options = []
    for i, sub_dir in enumerate(sub_dirs, start=1):
        options.append(i)
        print(f"{i}: {sub_dir.name}")
    user_inputs = ask_user()
    validate_category = validate_option(user_inputs, options)
    selected_category = sub_dirs[int(validate_category) - 1]
    return selected_category

# New recipe
def create_recipe():
    selected_category = show_categories()
    print("\n..:: Create a New Recipe ::..")
    print("\nEnter the name of the new recipe:")
    recipe_name = str(ask_user_text().strip())
    print("\nEnter the content of the recipe (press Enter twice to finish):")
    content = []
    while True:
        line = ask_user_text()
        if line == "":
            break
        content.append(line)
    recipe_path = guide / selected_category / f"{recipe_name}.txt"
    try:
        with open(recipe_path, "w") as file:
            file.write("\n".join(content))
        print(f"\nRecipe '{recipe_name}' created successfully in '{selected_category.name}'.")
    except Exception as e:
        print(f"Error creating the recipe: {e}")
    show_menu()

# New Category
def create_category():
    print("\n..:: Create a New Category ::..")
    print("\nEnter the name of the new category:")
    category_name = str(ask_user_text().strip())
    new_category_path = guide / category_name
    if new_category_path.exists():
        print(f"A category with the name '{category_name}' already exists.")
        return
    try:
        new_category_path.mkdir()
        print(f"\nCategory '{category_name}' created successfully.")
    except Exception as e:
        print(f"Error creating the category: {e}")
    show_menu()

# Delete Recipe
def delete_recipe(category):
    recipes = list(category.glob("*.txt"))
    options = []
    print("\n..:: Recipes ::..")
    for j, recipe in enumerate(recipes, start=1):
        options.append(j)
        print(f"{j}: {recipe.stem}")
    user_input = ask_user()
    validate_recipe = validate_option(user_input, options)
    selected_recipe = recipes[int(validate_recipe) - 1]
    try:
        selected_recipe.unlink()
        print(f"\nRecipe '{selected_recipe.stem}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting the recipe: {e}")
    show_menu()

# Delete Category
def delete_category(category):
    try:
        if category.is_dir():
            shutil.rmtree(category)
            print(f"\nCategory '{category.name}' deleted successfully.")
        else:
            print(f"'{category.name}' is not a valid directory.")
    except Exception as e:
        print(f"Error deleting the category: {e}")
    show_menu()

# Show Menu
def show_menu():
    print("\n..:: MENU OPTIONS ::..")
    print("""Select one of the options:
    1. Read recipe
    2. Create recipe
    3. Create category
    4. Delete recipe
    5. Delete category
    6. Exit""")
    user_input = ask_user()
    validate_input = validate_option(user_input, [1, 2, 3, 4, 5, 6])
    return validate_input

# START PROGRAM
print("Recipes Located at:", recipes_location)
print(" ####################   WELCOME TO KLEE RECIPES   #################### \n")
print("..:: Categories ::..")
get_category_recipe()
validate_input = show_menu()
while validate_input != 6:
    match validate_input:
        case 1:
            category = show_categories()
            show_recipes(category)
        case 2:
            create_recipe()
        case 3:
            create_category()
        case 4:
            category = show_categories()
            delete_recipe(category)
        case 5:
            category = show_categories()
            delete_category(category)
        case 6:
            print("Bye")
            exit(0)






























