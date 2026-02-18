### arguments to call specific functions ###
"""
"dice" to roll n [die]-sided dice
"100" to make a cast of [percent] percent probability
"cast" to make a cast on a specified stat
"dmd" to make char take [dmd] points of damage
"heal" to heal [heal] points of damage
"tmp" to add temp hp
"inventory" to access the inventory; -a to append an item to it, -rm to remove an item from it, 
"""

from sys import argv
import importlib
import os
# to be implemented: choose a specific char's config file
# set char_name and stats in config.py
  
config = importlib.import_module("config")
cast_module = importlib.import_module("casts")
inv_module = importlib.import_module("inventory")
health_module = importlib.import_module("health")
actions_module = importlib.import_module("actions")

def char_setup():
    if not os.path.isdir(f"./{config.char_name}"):
        tmp = False
        while not tmp:
            answer = input(f"is this your character's name: '{config.char_name}'? y/n    ")
            try:    
                if config.y_or_n(answer):
                    os.makedirs(f"./{config.char_name}")
                    print(f"created a folder for your character named '{config.char_name}' in this directory. all data about your character will be saved there.\nplease don't touch it unless you know what you're doing.")
                    tmp = True
                else:
                    config.char_select()
                    char_setup()
                    return None
            except:
                print("invalid answer; please enter 'y' for 'yes' or 'n' for 'no'.")
    return None

def main():
    try:
        argv[1]
    except:
        print("please provide one of the following arguments:\n'dice' followed by die-type and n_dice to roll n dice\n or '100' followed by a percentage to make a cast on a percentage")
        quit()
    if argv[1] == "dice":
        try:
            argv[2]
            argv[3]
        except:
            print("to roll dice, please provide a die-type and the number of dice to be rolled as ints")
            quit()
        print(f"rolled {argv[3]} d{argv[2]} and got {cast_module.roll_dice(argv[2], argv[3])}")
    elif argv[1] == "100":
        try:
            argv[2]
        except:
            print("to make a cast, please provide a percentage in range 0 to 100")
            quit()
        if cast_module.probability(argv[2]):
            print("success")
        else:
            print("failure")
    elif argv[1] == "cast":
        try:
            stat = argv[2]
        except:
            print("you need to provide a stat as argument")
        result = cast_module.cast_on_stat(stat)
        if result == "nat20":
            print(f"cast on {stat}: nat20")
        elif result == "nat1":
            print(f"cast on {stat}: nat01")
        else:
            print(f"cast on {stat}: {result}")
    elif argv[1] == "dmg":
        try:
            dmg = int(argv[2])
            if dmg < 0:
                Exception
            else:
                health_module.take_dmg(dmg)
        except:
            print("invalid input; damage needs to be a positive int")
            quit()
    elif argv[1] == "heal":
        try:
            heal = int(argv[2])
            if heal < 0:
                Exception
            else:
                health_module.heal_dmg(heal)
        except:
            print("invalid input; damage healed needs to be a positive int")
            quit()
    elif argv[1] == "tmp":
        try:
            heal = int(argv[2])
            if heal < 0:
                Exception
            else:
                health_module.add_tmp_hp(heal)
        except:
            print("invalid input; temp added need to be a positive int")
            quit()
    elif argv[1] == "inv":
        try:
            if argv[2] == "-a":
                inv_module.add_item()
            elif argv[2] == "-rm":
                inv_module.remove_item()
            else:
                Exception
        except:
            print("invalid input; use '-a' to append an item or '-rm' to remove one")
            return None
    elif argv[1] == "set_char":
        pass
    else:
        print("invalid input; [manual is not yet implemented; call manual once implemented]")
    return None

def init():
    if config.char_select_on_startup:
        config.char_select()
    char_setup()
    health_module.init_health()
    inv_module.init_inventory()
    actions_module.init_actions()
    return None

# call main from within init() once the script is done
init()
#main()
# print(f"arguments: {argv}")