import importlib
config = importlib.import_module("config")
hp = None
hp_max = None
hp_tmp = None

# not yet implemented, but nice to have, anyway: resistances and effectiveness
# resistances and weaknesses could be implemented as an optional argument which is used as a key in a dict storing dmg multipliers for each dmg type, which is used to calc dmg
# dmg is cast to int in main()
def take_dmg(dmg):
    global hp, hp_max, hp_tmp
    temp = hp + hp_tmp - dmg
    if temp <= hp:
        hp = temp
        hp_tmp = 0
    else:
        hp_tmp -= dmg
    if hp <= 0:
        hp = 0
        print(f"{config.char_name} is dying!")
    with open(f"{config.char_name}/hp_{config.char_name}.txt", "w", encoding = "utf-8") as file:
        file.write(f"{hp}\n{hp_max}\n{hp_tmp}")
    return None

# heal is cast to int in main()
def heal_dmg(heal):
    global hp, hp_max, hp_tmp
    temp = hp + heal
    if temp >= hp_max:
        hp = hp_max
    else:
        hp = temp
    with open(f"{config.char_name}/hp_{config.char_name}.txt", "w", encoding = "utf-8") as file:
        file.write(f"{hp}\n{hp_max}\n{hp_tmp}")
    return None

# heal is cast to in in main()
def add_tmp_hp(heal):
    global hp, hp_max, hp_tmp
    if hp_tmp < heal:
        hp_tmp = heal
        with open(f"{config.char_name}/hp_{config.char_name}.txt", "w", encoding = "utf-8") as file:
            file.write(f"{hp}\n{hp_max}\n{hp_tmp}")
    return None

def set_and_check_hp():
    global hp, hp_max, hp_tmp
    tmp = False
    while not tmp:
        hp = input("please enter your current hp:    ")
        tmp, hp = config.is_pos_int(hp)
    tmp = False
    while not tmp:
        hp_max = input("please enter your max hp:    ")
        tmp, hp_max = config.is_pos_int(hp_max)
    tmp = False
    while not tmp:
        hp_tmp = input("please enter your temp hp:    ")
        tmp, hp_tmp = config.is_pos_int(hp_tmp)
    return None

def init_health():
    global hp, hp_max, hp_tmp
    try:
        with open(f"{config.char_name}/hp_{config.char_name}.txt", "r", encoding = "utf-8") as file:
            try:
                vals = file.read().strip().split()
                hp = int(vals[0])
                hp_max = int(vals[1])
                hp_tmp = int(vals[2])
            except:
                print("file is empty!")
                set_and_check_hp()
                with open(f"{config.char_name}/hp_{config.char_name}.txt", "w", encoding = "utf-8") as file:
                    file.write(f"{hp}\n{hp_max}\n{hp_tmp}")
                return None
    except:
        print(f"there is no file called {config.char_name}/hp_{config.char_name}.txt for saving and reading hp-values. initialize file creation...")
        try:
            set_and_check_hp()
            with open(f"{config.char_name}/hp_{config.char_name}.txt", "x", encoding = "utf-8") as file:
                file.write(f"{hp}\n{hp_max}\n{hp_tmp}")
        except:
            print("your hp values need to be positive ints! max hp needs to be greater than 0!")
    return None

#init_health()