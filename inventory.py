import json
import importlib
config = importlib.import_module("config")
display_module = importlib.import_module("display")

inventory = {}
dir = ""

def create_inventory():
    try:
        with open(f"{dir}/{config.char_name}/inventory_{config.char_name}.json", 'x') as file:
            json.dump(inventory, file, indent = 4)
    except:
        print(f"cannot create file {config.char_name}/inventory_{config.char_name}.json; a file with said name already exists in this directory")
    return None

def sort_inventory():
    global inventory
    inventory = dict(sorted(inventory.items()))
    return None

def init_inventory(module_dir):
    global inventory, dir
    dir = module_dir
    try:
        with open(f"{dir}/{config.char_name}/inventory_{config.char_name}.json", 'r') as file:
            inventory = json.load(file)
    except:
        create_inventory()
    return None

def add_item():
    global inventory
    item_name = input("please enter your item's name:    ")
    item_desc = input("please enter your item's description:    ")
    inventory[item_name] = item_desc
    sort_inventory()
    try:
        with open(f"{dir}/{config.char_name}/inventory_{config.char_name}.json", 'w') as file:
            json.dump(inventory, file, indent = 4)
    except:
        create_inventory()
    return print(f"{item_name} was successfully added to inventory!")

def remove_item():
    global inventory
    item_name = input("which item do you want to remove?    ")
    try:
        del inventory[item_name]
    except:
        print(f"there was no item named {item_name} in your inventory!")
        return None
    try:
        with open(f"{dir}/{config.char_name}/inventory_{config.char_name}.json", 'w') as file:
            json.dump(inventory, file, indent = 4)
    except:
        create_inventory()
    return print(f"{item_name} was successfully removed from inventory!")

def display_inventory():
    display_module.dict_keys(inventory, "inventory")
    return None

def display_item():
    name = input("which item do you want to display?    ")
    if name in inventory:
        display_module.dict_value_of_key(inventory, name)
    else:
        print(f"there is no item called '{name}' in your inventory!")
    return None

