import json
import os

### the following bools will be overridden with values from settings files (settings_global.json and settings_{char_name}.json) ###

# when set to True, you will be prompted to enter your character's name whenever starting this application; otherwise uses default name above
char_select_on_startup = False

# default character name; a name is required for accessing files
char_name = "liavyre"

# default value, overridden if char_select_on_startup; set to True if your character has spells, including cantrips
is_caster = True

# set to True if you want full attack properties; uses 'simplified' attacks by default
advanced_attack = False

# set to True if you want to see rolls for attacks and spells; shows only results by default
show_calculations = False

settings_global = {
    "char_select_on_startup" : char_select_on_startup,
    "char_name" : char_name,
    "show_calculations" : show_calculations
}
settings_character = {
    "is_caster" : is_caster,
    "advanced_attacks" : advanced_attack
}

### do not touch below here ###

# utility

def is_pos_int(num):
    try:
        num = int(num)
    except:
        print("your input needs to be a positive integer.")
        return False, 0
    if num < 0:
        print("your input needs to be a positive integer.")
        return False, 0
    else:
        return True, num

def y_or_n(answer):
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        Exception

# character selection

def char_select():
    global char_name
    char_name = input("please enter your character's name:    ")
    return None

# change settings

def save_global_settings():
    with open(f"settings.json", 'w') as file:
        json.dump(settings_global, file, indent = 4)
    return None

def create_global_settings():
    print("creating global settings...")
    with open(f"settings.json", 'x') as file:
        json.dump(settings_global, file, indent = 4)
    return print("global settings file created")

def save_char_settings():
    with open(f"{char_name}/settings_{char_name}.json", 'w') as file:
        json.dump(settings_character, file, indent = 4)
    return None

def create_char_settings():
    with open(f"{char_name}/settings_{char_name}.json", 'x') as file:
        json.dump(settings_character, file, indent = 4)
    return None

def set_is_caster():
    global is_caster
    tmp = False
    while not tmp:
        answer = input("is your character a caster? y/n    ")
        try:
            is_caster = y_or_n(answer)
            save_char_settings()
            print(f"is_caster is now set to '{is_caster}'")
            tmp = True
        except:
            print("invalid input; please enter 'y' for 'yes' or 'n' for 'no'!")
    return None

def set_advanced_attack():
    global advanced_attack
    tmp = False
    while not tmp:
        answer = input("do you want to use advanced attack descriptions?\nthis will not change actions already set retroactively!\ny/n    ")
        try:
            advanced_attack = y_or_n(answer)
            save_char_settings()
            print(f"advanced_attack is now set to '{advanced_attack}'")
            tmp = True
        except:
            print("invalid input; please enter 'y' for 'yes' or 'n' for 'no'!")
    return None

def set_show_calculations():
    global show_calculations
    tmp = False
    while not tmp:
        answer = input("do you want to show details like indicidual die casts and calculations? y/n    ")
        try:
            show_calculations = y_or_n(answer)
            save_char_settings()
            print(f"show_calculations is now set to '{show_calculations}'")
            tmp = True
        except:
            print("invalid input; please enter 'y' for 'yes' or 'n' for 'no'!")
    return None

def change_character():
    global char_name
    tmp = False
    while not tmp:
        answer = input("are you sure you want to change your character?\nthis will cause the script to reinitialize to change data across the application.\ny/n    ")
        try:
            answer = y_or_n(answer)
            tmp = True
        except:
            print("invalid answer! please enter 'y' for 'yes' or 'n' for 'no'!")
    char_name = input("which character do you want to load?    ")
    while not tmp:
        answer = input(f"set {char_name} as your new default character? y/n    ")
        try:
            answer = y_or_n(answer)
            tmp = True
        except:
            print("invalid answer! please enter 'y' for 'yes' or 'n' for 'no'!")
    if answer:
        save_global_settings()
    return None

def set_char_select_on_startup():
    global char_select_on_startup
    tmp = False
    while not tmp:
        answer = input("do you want to select your character each time starting this application? y/n    ")
        try:
            char_select_on_startup = y_or_n(answer)
            save_global_settings()
            print(f"char_select_on_startup is now set to '{char_select_on_startup}'")
            tmp = True
        except:
            print("invalid input; please enter 'y' for 'yes' or 'n' for 'no'!")
    return None

def update_global_settings():
    global settings_global, char_select_on_startup, char_name, show_calculations
    settings_global = {
        "char_select_on_startup" : char_select_on_startup,
        "char_name" : char_name,
        "show_calculations" : show_calculations
    }
    return None

def update_char_settings():
    global settings_character, is_caster, advanced_attack
    settings_character = {
        "is_caster" : is_caster,
        "advanced_attack" : advanced_attack
    }
    return None

def char_setup():
    if not os.path.isdir(f"./{char_name}"):
        tmp = False
        while not tmp:
            answer = input(f"is this your character's name: '{char_name}'? y/n    ")
            try:    
                if y_or_n(answer):
                    os.makedirs(f"./{char_name}")
                    print(f"created a folder for your character named '{char_name}' in this directory. all data about your character will be saved there.\nplease don't touch it unless you know what you're doing.")
                    tmp = True
                else:
                    char_select()
                    char_setup()
                    return None
            except:
                print("invalid answer; please enter 'y' for 'yes' or 'n' for 'no'.")
    return None

def init_settings():
    global settings_global, settings_character, char_select_on_startup, char_name, is_caster, advanced_attack, show_calculations
    try:
        with open(f"settings.json", 'r') as file:
            settings_global = json.load(file)
        char_select_on_startup = settings_global["char_select_on_startup"]
        char_name = settings_global["char_name"]
        show_calculations = settings_global["show_calculations"]
    except:
        print("no global settings have been found. initating first time setup...")
        char_name = input("please enter your character name:    ")
        tmp = False
        while not tmp:
            answer = input("do you want to select your character each time starting this application? y/n    ")
            try:
                char_select_on_startup = y_or_n(answer)
                tmp = True
            except:
                print("invalid input; please enter 'y' for 'yes' or 'n' for 'no'!")
        update_global_settings()
        create_global_settings()
    try:
        with open(f"{char_name}/settings_{char_name}.json", 'r') as file:
            settings_character = json.load(file)
        is_caster = settings_character["is_caster"]
        advanced_attack = settings_character["advanced_attack"]
    except:
        print(f"no settings for a character name '{char_name}' have been found. initializing character setup...")
        tmp = False
        while not tmp:
            answer = input("is your character a caster? y/n    ")
            try:
                is_caster = y_or_n(answer)
                tmp = True
            except:
                print("invalid input; please enter 'y' for 'yes' or 'n' for 'no'!")
        update_char_settings()
        char_setup()
        create_char_settings()
    return None

