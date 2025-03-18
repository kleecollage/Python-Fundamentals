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
import shutil
from pathlib import Path

dir_path = Path.cwd()
recipes_location = dir_path / "Recetas"
sub_dirs = [d for d in recipes_location.iterdir() if d.is_dir()]

# Show Menu
def show_menu():
    options = {
        1: "Read recipe",
        2: "Create recipe",
        3: "Create category",
        4: "Delete recipe",
        5: "Delete category",
        6: "Exit",
    }
    print("\n..:: MENU OPTIONS ::..")
    for key, value in options.items():
        print(f"{key}: {value}")
    return validate_option(ask_user(), options.keys())

# Get Categories
def get_category_recipe():
    total_recipes = sum(len(list(d.glob("*.txt"))) for d in sub_dirs)
    for sub_dir in sub_dirs:
        print(f"{sub_dir.name}: {len(list(sub_dir.glob('*.txt')))} recipes")
    print("Total:", total_recipes)

# Numeric User choice
def ask_user():
    while True:
        try:
            return int(input(">>> "))
        except ValueError:
            print("Invalid input. Please enter a number.")
# User Text Input
def ask_user_text():
   return input(">>> ").strip()

# Validate option
def validate_option(user_input, options):
    while user_input not in options:
        print("Sorry, that option is not valid. Please try again.")
        user_input = ask_user()
    return user_input

# Show recipes
def show_recipes(category):
    recipes = list(category.glob("*.txt"))
    if not recipes:
        print("No recipes found.")
        return

    print("\n..:: Recipes ::..")
    for idx, recipe in enumerate(recipes, start=1):
        print(f"{idx}: {recipe.stem}")

    selected_recipe = recipes[validate_option(ask_user(), range(1, len(recipes) + 1)) - 1]
    print(f"\nReading recipe: {selected_recipe.stem}\n")
    print(selected_recipe.read_text())

# Show categories
def show_categories():
    print("Choose the category")
    for idx, sub_dir in enumerate(sub_dirs, start=1):
        print(f"{idx}: {sub_dir.name}")
    return sub_dirs[validate_option(ask_user(), range(1, len(sub_dirs) + 1)) - 1]

# New recipe
def create_recipe():
    print("\n..:: Create a New Recipe ::..")
    category = show_categories()
    print("Enter the name of the new recipe")
    recipe_name = ask_user_text()
    print("Enter recipe content (press Enter twice to finish):")
    content = "\n".join(iter(ask_user_text, ""))
    recipe_path = category / f"{recipe_name}.txt"
    recipe_path.write_text(content)
    print(f"Recipe '{recipe_name}' created successfully in '{category.name}'.")

# New Category
def create_category():
    print("\n..:: Create a New Category ::..")
    print("\nEnter the name of the new category:")
    category_name = ask_user_text()
    category_path = recipes_location / category_name
    if category_path.exists():
        print(f"Category '{category_name}' already exists.")
    else:
        category_path.mkdir()
        print(f"Category '{category_name}' created successfully.")

# Delete Recipe
def delete_recipe(category):
    print("\n..:: Recipes ::..")
    recipes = list(category.glob("*.txt"))
    if not recipes:
        print("No recipes found.")
        return

    for idx, recipe in enumerate(recipes, start=1):
        print(f"{idx}: {recipe.stem}")

    selected_recipe = recipes[validate_option(ask_user(), range(1, len(recipes) + 1)) - 1]
    selected_recipe.unlink()
    print(f"Recipe '{selected_recipe.stem}' deleted successfully.")

# Delete Category
def delete_category(category):
    shutil.rmtree(category)
    print(f"Category '{category.name}' deleted successfully.")

# START PROGRAM
print("Recipes Located at:", recipes_location)
print(" ####################   WELCOME TO KLEE RECIPES   #################### \n")
print("..:: Categories ::..")
get_category_recipe()

while (option := show_menu()) != 6:
    match option:
        case 1: show_recipes(show_categories())
        case 2: create_recipe()
        case 3: create_category()
        case 4: delete_recipe(show_categories())
        case 5: delete_category(show_categories())
    print("Bye")