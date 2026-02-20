import importlib
import json
config = importlib.import_module("config")

artifact_abilities = {}

def sort_artifact_abilities():
    global artifact_abilities
    artifact_abilities = dict(sorted(artifact_abilities.items()))
    return artifact_abilities

def add_artifact_ability():
    global artifact_abilities
    slot_key = input("please enter the name of the artifact ability you want to add:    ")
    if slot_key in artifact_abilities:
        print("this artifact ability was already added!")
        return None
    tmp = False
    while not tmp:
        n_slots = input("how often can this ability be used before recharching?    ")
        tmp, n_slots = config.is_pos_int(n_slots)
    desc = input("please enter a description of your artifact ability:    ")
    tmp = False
    while not tmp:
        recharge_on_short_rest = input("does it recharge on short rests or only on longe ones? y/n    ")
        if recharge_on_short_rest == 'y':
            artifact_abilities[slot_key] = (n_slots, n_slots, True, desc)
            tmp = True
        elif recharge_on_short_rest == 'n':
            artifact_abilities[slot_key] = (n_slots, n_slots, False, desc)
            tmp = True
        else:
            print("that is not a valid answer! answer 'y' for 'yes' or 'n' for 'no'!")
    artifact_abilities = sort_artifact_abilities()
    with open(f"{config.char_name}/artifacts_{config.char_name}.json", 'w') as file:
            json.dump(artifact_abilities, file, indent = 4)
    return print(f"your artifact ability '{slot_key}' has successfully been added!")

def remove_artifact_ability():
    global artifact_abilities
    slot_key = input("please enter the name of the artifact ability you want to remove:    ")
    if not slot_key in artifact_abilities:
        print(f"an ability with the name {slot_key} has not been added!")
        return None
    del artifact_abilities[slot_key]
    with open(f"{config.char_name}/artifacts_{config.char_name}.json", 'w') as file:
            json.dump(artifact_abilities, file, indent = 4)
    return print(f"your artifact ability '{slot_key}' has successfully been removed!")

def create_artifacts():
    print(f"cannot retrieve artifact abilities from {config.char_name}/abilities_{config.char_name}.json; no file with said name exists in this directory. would you like to create one?")
    answer = input("y/n    ")
    if answer == "y":
        try:
            with open(f"{config.char_name}/artifacts_{config.char_name}.json", 'x') as file:
                json.dump(artifact_abilities, file, indent = 4)
        except:
            print(f"cannot create file {config.char_name}/artifacts_{config.char_name}.json; a file with said name already exists in this directory")
    return None

def use_artifact_ability():
    global artifact_abilities
    slot_key = input("which ability do you want to use?    ")
    if not slot_key in artifact_abilities:
        print(f"an ability with the name {slot_key} has not been added!")
        return None
    tmp = artifact_abilities[slot_key][0]
    if tmp > 0:
        artifact_abilities[slot_key][0] = tmp - 1
        with open(f"{config.char_name}/artifacts_{config.char_name}.json", 'w') as file:
            json.dump(artifact_abilities, file, indent = 4)
    else:
        if artifact_abilities[slot_key][2]:
            print("you're out of slots for your ability! your slots will be reset on your next short rest!")
        else:
            print("you're out of slots for your ability! your slots will be reset on your next long rest!")
    return None


def init_artifact_abilities():
    global artifact_abilities
    try:
        with open(f"{config.char_name}/artifacts_{config.char_name}.json", 'r') as file:
            artifact_abilities = json.load(file)
    except:
        create_artifacts()
    return None

