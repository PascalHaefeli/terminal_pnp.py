import importlib
config = importlib.import_module("config")
inventory = []

from sys import argv
import json

def create_inventory():
    print(f"cannot retrieve inventory from {config.char_name}/inventory_{config.char_name}.json; no file with said name exists in this directory. would you like to create one?")
    answer = input("y/n    ")
    if answer == "y":
        try:
            with open(f"{config.char_name}/inventory_{config.char_name}.json", 'x') as file:
                json.dump(inventory, file, indent = 4)
        except:
            print(f"cannot create file {config.char_name}/inventory_{config.char_name}.json; a file with said name already exists in this directory")
    return None

def init_inventory():
    global inventory
    try:
        with open(f"{config.char_name}/inventory_{config.char_name}.json", 'r') as file:
            inventory = json.load(file)
    except:
        create_inventory()
    return None

def add_item():
    global inventory
    item_name = input("please enter your item's name:    ")
    item_desc = input("please enter your item's description:    ")
    item = {"name": item_name, "description": item_desc}
    inventory.append(item)
    inventory.sort(key = lambda x: x["name"].lower())    # sorts inventory alphabetically before updating it in .json
    try:
        with open(f"{config.char_name}/inventory_{config.char_name}.json", 'w') as file:
            json.dump(inventory, file, indent = 4)
    except:
        create_inventory()
    return None

def remove_item():
    global inventory
    inventory = [item for item in inventory if item["name"].lower() != argv[3].lower()]
    try:
        with open(f"{config.char_name}/inventory_{config.char_name}.json", 'w') as file:
            json.dump(inventory, file, indent = 4)
    except:
        create_inventory()
    return None

