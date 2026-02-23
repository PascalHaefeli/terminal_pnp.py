import json
import importlib
config = importlib.import_module("config")

# don't touch this!
prf = {
    "initiative": 1,
    "str_save": 0,
    "dex_save": 0,
    "con_save": 0,
    "int_save": 0,
    "wis_save": 1,
    "cha_save": 1,
    "acrobatics": 0,
    "animal_handling": 0,
    "arcana": 1,
    "athletics": 0,
    "deception": 1,
    "history": 0,
    "insight": 0,
    "intimidation": 1,
    "investigation": 0,
    "medicine": 0,
    "nature": 0,
    "perception": 1,
    "performance": 1,
    "persuasion": 1,
    "religion": 0,
    "sleight_of_hand": 1,
    "stealth": 1,
    "survival": 0,
    "pas_perception": 0,
    "pas_investigation": 0,
    "pas_insight": 0
}

def save_prfs():
    with open(f"{config.char_name}/prfs_{config.char_name}.json", 'w') as file:
        json.dump(prf, file, indent = 4)
    return None

def create_prfs_file():
    print(f"no file with proficiencies for {config.char_name} was found. initiating proficiency setup...")
    proficiencies_setup()
    with open(f"{config.char_name}/prfs_{config.char_name}.json", 'x') as file:
        json.dump(prf, file, indent = 4)
    return None

def load_prfs():
    global prf
    try:
        with open(f"{config.char_name}/prfs_{config.char_name}.json", 'r') as file:
            prf = json.load(file)
    except:
        create_prfs_file()
    return None

def set_prf():
    global prf
    tmp = False
    while not tmp:
        proficiency = input("which proficiency modifier do you want to set:    ")
        try:
            proficiency = int(proficiency)
            tmp = True
        except:
            print("all proficiency modifiers need to be integers!")
    save_prfs()
    return None

def proficiencies_setup():
    for i in prf:
        tmp = False
        while not tmp:
            try:
                prf[i] = int(input(f"{i}:    "))
                tmp = True
            except:
                print("all proficiency modifiers need to be integers!")
    return None

def init_proficiencies():
    load_prfs()
    return None

