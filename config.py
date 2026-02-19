# default character name; a name is required for accessing files
char_name = "liavyre"

# when set to True, you will be prompted to enter your character's name whenever starting this application; otherwise uses default name above
char_select_on_startup = False

# set to True if your character has spells, including cantrips
is_caster = True

# set to True if you want full attack properties; uses 'simplified' attacks by default
advanced_attack = False

# set to True if you want to see rolls for attacks and spells; shows only results by default
show_calculations = False


# below variables are not yet in use; nice to have, might implement that later, but who keeps track of ammo and weight, anyway?
track_weight = False
track_ammo = False

### do not touch below here ###

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

def char_select():
    global char_name, is_caster
    char_name = input("please enter your character's name:    ")
    tmp = False
    while not tmp:
        is_caster = input("is your character a caster? y/n    ")
        tmp = y_or_n(is_caster)
        if tmp:
            is_caster = True
            tmp = True
        elif tmp == False:
            is_caster = False
            tmp = True
        else:
            print("invalid input! please enter 'y' for 'yes' or 'n' for 'no'.")
    return None

