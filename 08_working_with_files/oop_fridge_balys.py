import json

class Product:
    def __init__(self, name:str, quantity:float, unit_of_measurement:str = 'unit', **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = unit_of_measurement
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"


class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product: Product):
        ingredient_id, existing_product = self.check_ingredient(product.name)
        if existing_product is not None:
            existing_product.quantity += product.quantity
            print(f"{existing_product.name} was already in the recipe, and we added {product.quantity} more.")
        else:
            self.ingredients.append(Product(product.name, product.quantity, product.unit_of_measurement))
            print(f"{product.name}{product.quantity}{product.unit_of_measurement} was added to the recipe.")

    def check_ingredient(self, ingredient_name:str) -> (int, Product):
        for ingredient_id, ingredient in enumerate(self.ingredients):
            if ingredient_name.lower() == ingredient.name.lower():
                return ingredient_id, ingredient
        return None, None

    def remove_ingredient(self, name:str, quantity:float):
        self.print_recipe()
        ingredient_id, ingredient = self.check_ingredient(name)
        if ingredient is not None:
            if ingredient.quantity >= quantity:
                ingredient.quantity -= quantity
                print(f"{name}x{ingredient} was removed from recipe")
                if ingredient.quantity == 0:
                    self.ingredients.remove(ingredient)
                    print(f"All the {ingredient} was removed")
            else:
                print(f"Not enough {name} in the recipe.")
        else:
            print(f"Ingredient {name} does not exist in the recipe.")

    def print_recipe(self):
        for index, ingredient in enumerate(self.ingredients, start=1):
            print(f"{index}, {ingredient} {ingredient.unit_of_measurement}")

    def change_ingredient_quantity(self, name:str, quantity:float):
        product_id, ingredient = self.check_ingredient(name)
        if ingredient is not None:
            ingredient.name = name
            ingredient.quantity = quantity
            print(f"{name} x {quantity} {ingredient.unit_of_measurement}was added to recipe")
        else:
            print("Product does not exist in recipe")
        

class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name.lower() == product_name.lower():
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float, unit_of_measurement:str):
        product_id, product = self.check_product(name) 
        if product is not None:
            product.quantity += quantity
            print(f"{name} was already in the fridge and we added {quantity}{unit_of_measurement} more.")
        else:
            self.contents.append(Product(name, quantity, unit_of_measurement))
            print(f"{name}{quantity}{unit_of_measurement} was added to the fridge.")

    def print_contents(self):
        for index, line in enumerate(self.contents, start=1):
            print(f"{index} - {line} {line.unit_of_measurement}")

    def remove_product(self, name:str, quantity:float):
        self.print_contents()
        product_id, product = self.check_product(name)
        if product is not None:
            if product.quantity >= quantity:
                product.quantity -= quantity
                print(f"{quantity}x{product} was removed from fridge")
                if product.quantity == 0:
                    self.contents.remove(product)
                    print(f"All the {product} was removed")
            else:
                print(f"Not enough {name} in the fridge.")
        else:
            print(f"Product {name} does not exist in the fridge.")

    def check_recipe(self, recipe: Recipe):
            for ingredient in recipe.ingredients:
                index, fridge_product = self.check_product(ingredient.name)
                if fridge_product is None:
                    print(f"{ingredient.name} was not found in the fridge")
                    print("Recipe is not craftable")
                    return False
                quantity_difference = self.check_product_quantity(fridge_product, ingredient.quantity)
                if quantity_difference < 0:
                    print(f"Missing {abs(quantity_difference)}x{fridge_product.name}")
                    print("Recipe is not craftable")
                    return False
            print("Recipe is craftable")
            return True
    
    def save_to_file(self, filename='fridge_contents.json'):
        data = [{'name': product.name, 'quantity': product.quantity, 'unit_of_measurement': product.unit_of_measurement} for product in self.contents]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)

    def load_from_file(self, filename='fridge_contents.json'):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    product_instance = Product(**item)
                    self.contents.append(product_instance)
        except FileNotFoundError:
            print(f"No such file: {filename}")
    
def main():
    fridge = Fridge()
    recipe = Recipe()
    fridge.load_from_file()
    while True:
        print('''
-------------------- Main Fridge Menu --------------------
check - Checks fridge for a product
add - Add a new product
remove - Remove existing product
print - Prints the contents
recipe add - Add products to recipe
recipe remove - Remove products from recipe
recipe change - Change ingridient quantity of the recipe
recipe print - Print current recipe
recipe check - Check if recipe is craftable
exit - Exit
----------------------------------------------------------
              ''')
        choice = input("Your choice: ")
        if choice.startswith("exit"):
            fridge.save_to_file()
            break
        elif choice.startswith("check"):
            input_name = input("Input name: ")
            index, product = fridge.check_product(input_name)
            if index == None:
                print(f"{input_name} was not found in the fridge")
            else:
                print(f"{product} is item number:{index+1} in the fridge")
        elif choice.startswith("add"):
            input_name = input("Input name: ")
            input_quantity = float(input("Input quantity: "))
            input_unit_of_measurement = input("Input unit of measurment: ")
            fridge.add_product(input_name, input_quantity, input_unit_of_measurement)
        elif choice.startswith("remove"):
            if len(fridge.contents) == 0:
                print("Fridge is empty...")
            else:
                input_name = input("Input name: ")
                input_quantity = float(input("Input quantity: "))
                fridge.remove_product(input_name, input_quantity)
        elif choice.startswith("print"):
            if len(fridge.contents) == 0:
                print("Fridge is empty...")
            else:
                print("Current contents of the fridge:")
                fridge.print_contents()
        elif choice.startswith("recipe add"):
            input_recipe_name = input("Input product name: ")
            input_recipe_quantity = float(input("Input product quantity: "))
            input_unit_of_measurement = input("Input unit of measurment: ")
            input_product = Product(input_recipe_name, input_recipe_quantity, input_unit_of_measurement)
            recipe.add_ingredient(input_product)
        elif choice.startswith("recipe change"):
            input_ingridient_name = input("Input existing product name: ")
            input_ingridient_quantity = float(input("Input new product quantity: "))
            recipe.change_ingredient_quantity(input_ingridient_name, input_ingridient_quantity)
        elif choice.startswith("recipe remove"):
            if len(recipe.ingredients) == 0:
                print("Recipe is empty...")
            else:
                input_ingridient_name = input("Input product name: ")
                input_ingridient_quantity = float(input("Input product quantity: "))
                recipe.remove_ingredient(input_ingridient_name, input_ingridient_quantity)
        elif choice.startswith("recipe print"):
            if len(recipe.ingredients) == 0:
                print("Recipe is empty...")
            else:
                print("Contents of the recipe:")
                recipe.print_recipe()
        elif choice.startswith("recipe check"):
            if len(recipe.ingredients) ==0:
                print("Fridge is empty...")
            else:
                fridge.check_recipe(recipe)
        else:
            print("Bad choice, try again")



fridge = Fridge()
fridge.add_product("milk", 1.1, "l")
recipe = Recipe()
recipe.add_ingredient(Product("milk", 1.1, "l"))


if __name__ == "__main__":
    main()
