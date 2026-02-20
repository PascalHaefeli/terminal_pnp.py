### arguments to call specific functions ###
"""
"dice" to roll n [die]-sided dice
"100" to make a cast of [percent] percent probability
"cast" to make a cast on a specified stat
"dmg" to make char take [dmg] points of damage
"heal" to heal [heal] points of damage
"tmp" to add temp hp
"inv -a" to append an item to inventory
"inv -rm" to remove an item from from inventory
"act -a" to add an action
"act -rm" to remove an action
"act -mod" to modify an action
"atk" to perform an attack
"spell" to perform a spell
"spell -u" to perform a spell not listed as an action; only for spells that don't require casts by the caster's player
"slots" to modify max spell slots
"kat" to use liavyre's katana (liavyre only)
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

def short_rest():
    pass

def long_rest():
    pass

def input_loop():
    while True:
        command = input("your turn!    ")
        match command:
            case "q":
                print("exiting terminal_dnd.py...")
                quit()
            case "dice":
                cast_module.roll_dice()
            case "100":
                cast_module.probability()
            case "cast":
                cast_module.cast_on_stat()
            case "dmg":
                health_module.take_dmg()
            case "heal":
                health_module.heal_dmg()
            case "tmp":
                health_module.add_tmp_hp()
            case "inv -a":
                inv_module.add_item()
            case "inv -rm":
                inv_module.rm_item()
            case "act -a":
                actions_module.add_action()
            case "act -rm":
                actions_module.rm_action()
            case "act -mod":
                actions_module.mod_action()
            case "atk":
                actions_module.perform_attack()
            case "spell":
                actions_module.perform_spell()
            case "spell -u":
                actions_module.cast_unlisted_spell()
            case "slots":
                actions_module.mod_max_spell_slots()
            case "kat":
                actions_module.katana()
            

def init():
    if config.char_select_on_startup:
        config.char_select()
    char_setup()
    health_module.init_health()
    inv_module.init_inventory()
    actions_module.init_actions()
    input_loop()
    return None

# call input_loop() from within init() once the script is done
init()
#main()
# print(f"arguments: {argv}")