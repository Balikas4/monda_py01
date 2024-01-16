import pickle

def main(budget):
    while True:
        print('''
              ----Choose what you want to do with your budget----
                exit = Exit.
                add = Add new budget entry.
                remove = Removes a budget entry.
                list = Prints all budget entries.
                balance = Shows your budget balance
              ''')
        choice = input("Your choice: ")
        if choice.startswith("exit"):
            with open(r'D:\CodeAcademy\monda_py01\08_working_with_files\budget.pickle', 'wb') as file:
                pickle.dump(budget, file)
            break
        elif choice.startswith("add"):
            item_name = input("Item name:")
            item_quantity = float(input('Item quantity:'))
            insert_item(budget, item_name, item_quantity)
        elif choice.startswith("remove"):
            item_name = input("Item name:")
            item_quantity = float(input('Item quantity:'))
            remove_item(budget, item_name, item_quantity)
        elif choice.startswith("list"):
            print_items(budget)
        elif choice.startswith("balance"):
            get_balance(budget)
        else:
            print("Bad choice, try again")

def insert_item(budget, item_name: str, item_quantity: float):
    if item_name in budget:
        budget[item_name] += item_quantity
        print(f"{item_name} was already in the balance and we added {item_quantity} more.")
    else:
        budget[item_name] = item_quantity
        print(f"{item_quantity}x {item_name} was added to the balance.")

def remove_item(budget, item_name, item_quantity):
    if item_name in budget:
        if budget[item_name] >= item_quantity:
            budget[item_name] -= item_quantity
            if budget[item_name] == 0:
                del budget[item_name] 
            print(f"{item_name} was removed from the balance.")
        else:
            print(f"Not enough {item_name} quantity in the balance.")
    else:
        print(f"{item_name} does not exist in the balance.")
    return budget

def print_items(budget):
    print('Contents of the balance:')
    for index, (item_name, item_quantity) in enumerate(budget.items(), start=1):
        print(f'{index}. {item_name} : {item_quantity}')

def get_balance(budget):
    positive_balance = 0
    negative_balance = 0
    for item_name, item_quantity in budget.items():
        if item_quantity > 0:
            positive_balance += item_quantity
        else:
            negative_balance += item_quantity
    balance = positive_balance + negative_balance
    print(f"Your total gains: {positive_balance} minus your total loss: {negative_balance}\nYour ballance is: {balance}")
    return balance

if __name__ == "__main__":
    budget = {}
    try:
        with open(r"D:\CodeAcademy\monda_py01\08_working_with_files\budget.pickle", 'rb') as file:
            loaded_budget = pickle.load(file)
            print("File loaded successfully.")
            budget = loaded_budget
    except FileNotFoundError:
        print(f"The file does not exist.")
    main(budget)



""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""
