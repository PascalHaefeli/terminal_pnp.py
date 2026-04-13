from random import randint
import importlib
config = importlib.import_module("config")
# try except statement and creation of stats_{char_name}.py
stats_module = importlib.import_module(f"stats")

# rolls n [die]-sided dice
def roll_dice():
    tmp = False
    while not tmp:
        die_type = input("please enter the die type:    ")
        tmp, die_type = config.is_pos_int(die_type)
        if not tmp:
            print("the number of sides for your die must be a positive integer!")
    tmp = False
    while not tmp:
        n_dice = input(f"\nhow many d{die_type} do you want to roll?    ")
        tmp, n_dice = config.is_pos_int(n_dice)
        if not tmp:
            print("the amount of dice to roll needs to be a positive integer!")
    index = 0
    casts = []
    while index < n_dice:
        casts.append(randint(1, die_type))
        index += 1
    return casts

# rolls n [die]-sided dice
def roll_dice_script(die_type, n_dice):
    index = 0
    casts = []
    while index < n_dice:
        casts.append(randint(1, die_type))
        index += 1
    return casts

# makes a cast of [percent] percent
def probability():
    tmp = False
    while not tmp:
        try:
            percent = int(input("please enter the chance for a success as percentage:    "))
            if not 0 <= percent <= 100:
                print("percentages must be in range 0 to 100")
            else:
                tmp = True
        except:
            print("percentage must be of type int")                   
    cast = randint(1, 100)
    if config.show_calculations:
        print(f"cast: {cast}; pecentage: {percent}")
    return percent >= cast

def cast_on_stat():
    uncasteable = ["mv", "prf_mod", "spellcast_stat", "pact_slot_lv"]
    tmp = False
    while not tmp:
        stat = input("which stat do you want to cast on:    ")
        if stat not in stats_module.stats and not stat in uncasteable:
            print("invalid argument; please provide a valid stat from dnd to cast on")
        else:
             tmp = True
    cast = randint(1, 20)
    if cast == 20:
        return "nat20"
    elif cast == 1:
        return "nat1"
    mod = stats_module.get_stat(stat)
    return print(f"\ncast on {stat}: {cast + mod}")

cast_on_stat()