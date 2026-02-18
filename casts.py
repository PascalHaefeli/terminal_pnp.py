from random import randint
import importlib
config = importlib.import_module("config")
stats_module = importlib.import_module(f"{config.char_name}.stats_{config.char_name}")

# rolls n [die]-sided dice
def roll_dice(die, n_dice):
    tmp = False
    while not tmp:
        try:
            die = int(die)
            n_dice = int(n_dice)
            tmp = True
        except:
            print("die-type and n_dice must be of type int")
            die = input("please enter a valid die type:    ")
            n_dice = input("please enter a valid number of dice:    ")
    index = 0
    casts = []
    while index < int(n_dice):
        casts.append(randint(1, int(die)))
        index += 1
    return casts

# makes a cast of [percent] percent
def probability(percent):
    tmp = False
    while not tmp:
        try:
            percent = int(percent)
            if not 0 <= percent <= 100:
                print("percentages must be in range 0 to 100")
                percent = input("please enter a valid percentage:    ")
            else:
                tmp = True
        except:
            print("percentage must be of type int")
            percent = input("please enter a valid percentage:    ")                    
    cast = randint(1, 100)
    #print(cast)
    return percent >= cast

def cast_on_stat(stat):
    tmp = False
    while not tmp:
        if stat not in stats_module.stats:
            print("invalid argument; please provide a valid stat from dnd to cast on")
            stat = input("please provide a valid stat:    ")
        else:
             tmp = True
    cast = randint(1, 20)
    if cast == 20:
        return "nat20"
    elif cast == 1:
        return "nat1"
    mod = stats_module.get_stat(stat)
    return cast + mod

