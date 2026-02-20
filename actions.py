import importlib
import pickle
import json
import random
config = importlib.import_module("config")
cast_module = importlib.import_module("casts")
stats_module = importlib.import_module(f"{config.char_name}.stats_{config.char_name}")

# global variables

attacks = {}
spells = {}
spell_slots = {}
needs_int = ["die_type", "n_dice", "fixed_value", "fixed_save"]

# classes

class attack:
    
    def __init__(self, action_name, desc, n_dice, die_type, fixed_value, dmg_type, range, long_range, is_finesse, is_proficient, can_dual_wield):
        self.action_name = action_name
        self.desc = desc
        self.n_dice = n_dice
        self.die_type = die_type
        self.fixed_value = fixed_value
        self.dmg_type = dmg_type
        self.range = range
        self.long_range = long_range
        self.is_finesse = is_finesse
        self.is_proficient = is_proficient
        self.can_dual_wield = can_dual_wield

class attack_advanced:
    
    def __init__(self, action_name, desc, n_dice, die_type, fixed_value, dmg_type, range, long_range, is_finesse, is_proficient, can_dual_wield, aoe_type, aoe_size, activation_type, activation_time, affected_by_martial_arts):
        self.action_name = action_name
        self.desc = desc
        self.n_dice = n_dice
        self.die_type = die_type
        self.fixed_value = fixed_value
        self.dmg_type = dmg_type
        self.range = range
        self.long_range = long_range
        self.is_finesse = is_finesse
        self.is_proficient = is_proficient
        self.can_dual_wield = can_dual_wield
        self.aoe_type = aoe_type
        self.aoe_size = aoe_size
        self.activation_type = activation_type
        self.activation_time = activation_time
        self.affected_by_martial_arts = affected_by_martial_arts

class spell:

    def __init__(self, action_name, desc, n_dice, die_type, fixed_value, dmg_type, range, long_range, slot_lv, duration, save_type, fixed_save, needs_hit_cast, aoe_size, aoe_type):
        self.action_name = action_name
        self.desc = desc
        self.n_dice = n_dice
        self.die_type = die_type
        self.fixed_value = fixed_value
        self.dmg_type = dmg_type
        self.range = range
        self.long_range = long_range
        self.slot_lv = slot_lv
        self.duration = duration
        self.save_type = save_type
        self.fixed_save = fixed_save
        self.needs_hit_cast = needs_hit_cast
        self.aoe_size = aoe_size
        self.aoe_type = aoe_type

# spell slots

def init_spell_slots():
    print(f"no file named '{config.char_name}/spell_slots_{config.char_name}.json' exists in this directory. initiating setup of spell slots.\nif {config.char_name} is not a caster, terminate this application with ctrl + c and change 'is_caster' in config.py to 'False'.")
    try:
        tmp = int(input("number of lv_1 slots:    "))
        spell_slots['1'] = (tmp, tmp)
        tmp = int(input("number of lv_2 slots:    "))
        spell_slots['2'] = (tmp, tmp)
        tmp = int(input("number of lv_3 slots:    "))
        spell_slots['3'] = (tmp, tmp)
        tmp = int(input("number of lv_4 slots:    "))
        spell_slots['4'] = (tmp, tmp)
        tmp = int(input("number of lv_5 slots:    "))
        spell_slots['5'] = (tmp, tmp)
        tmp = int(input("number of lv_6 slots:    "))
        spell_slots['6'] = (tmp, tmp)
        tmp = int(input("number of lv_7 slots:    "))
        spell_slots['7'] = (tmp, tmp)
        tmp = int(input("number of lv_8 slots:    "))
        spell_slots['8'] = (tmp, tmp)
        tmp = int(input("number of lv_9 slots:    "))
        spell_slots['9'] = (tmp, tmp)
        tmp = int(input("number of pact slots:    "))
        spell_slots['p'] = (tmp, tmp)
    except:
        print("the number of each spell slot must be a positive int!") # i'm not actually checking for positive ints, but who cares? if it's negative, it'll be < 1, so it's the same as '0'
        init_spell_slots()
        return None
    with open(f"{config.char_name}/spell_slots_{config.char_name}.json", 'x') as slots:
        json.dump(spell_slots, slots, indent = 4)
    return print("spell slots initialized successfully!")

def mod_max_spell_slots():
    slot = input("which spell slot do you want to modify?    ")
    if slot == 'p' or config.is_pos_int(slot)[0]:
        tmp = input("please enter the new value for this spell slot:    ")
        tmp2, tmp = config.is_pos_int(tmp)
        if tmp2:
            spell_slots[slot][1] = tmp
            with open(f"{config.char_name}/spell_slots_{config.char_name}.json", 'w') as slots:
                json.dump(spell_slots, slots, indent = 4)
                return print(f"slot '{slot}' has been set to the new max of {tmp}")
        else:
            print("max spell slots must be positive integers!")
            return mod_max_spell_slots()
    else:
        print("spell slots must be positive integers or 'p' for 'pact slot'!")
        return mod_max_spell_slots()

def reset_spell_slots():
    global spell_slots
    for i in spell_slots:
        spell_slots[i][0] = spell_slots[i][1]
    with open(f"{config.char_name}/spell_slots_{config.char_name}.json", 'w') as slots:
        json.dump(spell_slots, slots, indent = 4)
    return print(f"all spell slots have been reset!")
    
def reset_pact_slots():
    global spell_slots
    spell_slots['p'][0] = spell_slots['p'][1]
    with open(f"{config.char_name}/spell_slots_{config.char_name}.json", 'w') as slots:
        json.dump(spell_slots, slots, indent = 4)
    return print(f"pact slots have been reset!")

def occupy_spell_slot(slot_lv):
    global spell_slots
    tmp = spell_slots[slot_lv][0]
    spell_slots[slot_lv][0] = tmp - 1
    with open(f"{config.char_name}/spell_slots_{config.char_name}.json", 'w') as slots:
        json.dump(spell_slots, slots, indent = 4)
    return None

def wild_magic(is_cantrip):
    if is_cantrip:
        if random.randint(1, 100) == 1:
            print("a wild magic appears!")
            return True
    else:
        if random.randint(1, 20) == 1:
            print("a wild magic appears!")
            return True
    return False

def cast_unlisted_spell():
    slot_lv = input("which level is the spell you want to cast? '0' for cantrips, 'p' for pact spells:    ")
    if slot_lv != '0':
        occupy_spell_slot(slot_lv)
        wild_magic(False)
    else:
        wild_magic(True)
    return print(f"one category {slot_lv} slot has been occupied.")

# manage actions

def init_actions():
    global attacks, spells, spell_slots
    try:
        with open(f"{config.char_name}/attacks_{config.char_name}.pkl", "rb") as atks:
            attacks = pickle.load(atks)
    except:
        with open(f"{config.char_name}/attacks_{config.char_name}.pkl", "wb") as atks:
            pickle.dump(attacks, atks)
    try:
        with open(f"{config.char_name}/spells_{config.char_name}.pkl", "rb") as spls:
            spells = pickle.load(spls)
    except:
        with open(f"{config.char_name}/spells_{config.char_name}.pkl", "wb") as spls:
            pickle.dump(spells, spls)
    if config.is_caster:
        try:
            with open(f"{config.char_name}/spell_slots_{config.char_name}.json", 'r') as slots:
                spell_slots = json.load(slots)
        except:
            init_spell_slots()
    return None

def sort_actions(action_type):
    global attacks, spells
    if action_type == "attack":
        attacks = dict(sorted(attacks.items()))
        return attacks
    elif action_type == "spell":
        spells = dict(sorted(spells.items()))
        return spells

def add_action():
    global attacks, spells
    # any action type
    tmp = False
    # specify action type
    while not tmp:
        action_type = input("please specify the action you want to add: 'a' for 'attack', 's' for 'spell':    ")
        if action_type == 'a' or action_type == 's':
            tmp = True
        else:
            print("that's not a valid action type.")
    action_name = input("please enter your action's name:    ")
    desc = input("please enter a description to your action:    ")
    tmp = False
    # specify die_type, n_dice and fixed_value
    while not tmp:
        die_type = input("please enter your die type for damage casts:    ")
        tmp, die_type = config.is_pos_int(die_type)
    tmp = False
    while not tmp:
        n_dice = input("please enter how many dice are rolled for damage casts:    ")
        tmp, n_dice = config.is_pos_int(n_dice)
    tmp = False
    while not tmp:
        fixed_value = input("please enter a fixed value for damage casts:    ")
        tmp, fixed_value = config.is_pos_int(fixed_value)
    dmg_type = input("please enter the type of damage dealt by your action:    ")
    range = input("please enter your action's range:    ")
    long_range = input("please enter your action's long range:    ")
    action_set = False
    # check which action is to be created
    while not action_set:
        # any attack
        if action_type == 'a':
            tmp = False
            while not tmp:
                is_finesse = ("is your 'weapon' a finesse weapon? y/n    ")
                try:
                    is_finesse = config.y_or_n(is_finesse)
                    tmp = True
                except:
                    print("that's not a valid answer.")
            tmp = False
            while not tmp:
                is_proficient = input("is your character proficient with their 'weapon'? y/n    ")
                try:
                    is_proficient = config.y_or_n(is_proficient)
                    tmp = True
                except:
                    print("that's not a valid answer.")
            tmp = False
            while not tmp:
                can_dual_wield = input("can your 'weapon' be dual wielded? y/n    ")
                try:
                    can_dual_wield = config.y_or_n(can_dual_wield)
                    tmp = True
                except:
                    print("that's not a valid answer.")
            # advanced attack
            if config.advanced_attack:
                aoe_type = input("please enter your attack's aoe type:    ")
                aoe_size = input("please enter your attack's aoe size:    ")
                activation_type = input("please enter your activation type:    ")
                activation_time = input("please enter your activation time:    ")
                affected_by_martial_arts = input("is your attack affected by martial arts? y/n    ")
                #exec(f"{action_name} = attack_advanced({action_name}, {desc}, {n_dice}, {die_type}, {fixed_value}, {dmg_type}, {range}, {long_range}, {is_finesse}, {is_proficient}, {can_dual_wield}, {aoe_type}, {aoe_size}, {activation_type}, {activation_time}, {affected_by_martial_arts})")
                instance = attack_advanced(
                    action_name, 
                    desc, 
                    n_dice, 
                    die_type, 
                    fixed_value, 
                    dmg_type, 
                    range, 
                    long_range, 
                    is_finesse, 
                    is_proficient, 
                    can_dual_wield, 
                    aoe_type, 
                    aoe_size, 
                    activation_type, 
                    activation_time, 
                    affected_by_martial_arts
                    )
                attacks[action_name] = instance
                action_set = True
                print(f"{action_name} set as an advanced attack")
            # standard attack
            else:
                #exec(f"{action_name} = attack({action_name}, {desc}, {n_dice}, {die_type}, {fixed_value}, {dmg_type}, {range}, {long_range}, {is_finesse}, {is_proficient}, {can_dual_wield})")
                instance = attack(
                    action_name, 
                    desc, 
                    n_dice, 
                    die_type, 
                    fixed_value, 
                    dmg_type, 
                    range, 
                    long_range, 
                    is_finesse, 
                    is_proficient, 
                    can_dual_wield
                    )
                action_set = True
                attacks[action_name] = instance
                print(f"{action_name} has been set as an attack")
            print(f"{action_name} = {attacks[action_name]}")
            sort_actions("attack")
            # write current attacks dict to pkl file in binary
            with open(f"{config.char_name}/attacks_{config.char_name}.pkl", "wb") as atks:
                pickle.dump(attacks, atks)
        # spell
        elif action_type == 's':
            tmp = False
            while not tmp:
                slot_lv = input("what level is your spell? enter '0' if it's a cantrip:    ")
                try:
                    if slot_lv != "p":
                        slot_lv = int(slot_lv)
                except:
                    print("your spell's level must be an integer or 'p', if its a pact spell.")
                if 0 <= slot_lv <= 9 or slot_lv == "p":
                    tmp = True
                else:
                    print("your spell's level must be an integer in between 0 (cantrip) and 9 (highest possible spell level).")
            duration = input("please enter your spells duration:    ")
            save_type = input("please enter your save type:    ")
            fixed_save = input("please enter your fixed save:    ")
            aoe_size = input("please enter your aoe_size:    ")
            aoe_type = input("please enter your aoe_type:    ")
            tmp = False
            while not tmp:
                needs_hit_cast = input("does your spell require a hit cast? y/n    ")
                try:
                    is_finesse = config.y_or_n(needs_hit_cast)
                    tmp = True
                except:
                    print("that's not a valid answer.")
            #exec(f"{action_name} = spell({action_name}, {desc}, {n_dice}, {die_type}, {fixed_value}, {dmg_type}, {range}, {long_range}, {slot_lv}, {duration}, {save_type}, {fixed_save}, {needs_hit_cast})")
            instance = spell(
                action_name, 
                desc, 
                n_dice, 
                die_type, 
                fixed_value, 
                dmg_type, 
                range, 
                long_range, 
                slot_lv, 
                duration, 
                save_type, 
                fixed_save, 
                needs_hit_cast,
                aoe_size,
                aoe_type
                )
            spells[action_name] = instance
            print(f"{action_name} has been set as a spell")
            action_set = True
            print(f"{action_name} = {spells[action_name]}")
            sort_actions("spell")
            with open(f"{config.char_name}/spells_{config.char_name}.pkl", "wb") as spls:
                pickle.dump(spells, spls)
    return None

def rm_action():
    global attacks, spells
    # pick action type
    tmp = False
    while not tmp:
        action_type = input("please specify the type of action you want to remove: 'a' for 'attack', 's' for 'spell':    ")
        if action_type == 'a' or action_type == 's':
            tmp = True
        else:
            print("that's not a valid action type.")
    action_name = input("which action do you want to remove:    ")
    # attacks
    if action_type == 'a':
        try:
            del attacks[action_name]
            sort_actions("attack")
            with open(f"{config.char_name}/attacks_{config.char_name}.pkl", "wb") as atks:
                pickle.dump(attacks, atks)
        except:
            print("no attack with the specified name was set for this character!")
    # spells
    else:
        try:
            del spells[action_name]
            sort_actions("spell")
            with open(f"{config.char_name}/spells_{config.char_name}.pkl", "wb") as spls:
                pickle.dump(spells, spls)
        except:
            print("no spell with the specified name was set for this character!")
    return None

def mod_action():
    global attacks, spells, needs_int
    # pick action type
    tmp = False
    while not tmp:
        action_type = input("please specify the type of action you want to modify: 'a' for 'attack', 's' for 'spell':    ")
        if action_type == 'a' or action_type == 's':
            tmp = True
        else:
            print("that's not a valid action type.")
    action_name = input("which action do you want to modify:    ")
    var_name = input("which attribute do you want to modify:    ")
    tmp = False
    while not tmp:
        new_value = input(f"please enter a new value for '{var_name}':    ")
        if var_name in needs_int:
            tmp, new_value = config.is_pos_int(new_value)              
    # attacks
    if action_type == 'a':
        if hasattr(attacks[action_name], var_name):
            setattr(attacks[action_name], var_name, new_value)
            with open(f"{config.char_name}/attacks_{config.char_name}.pkl", "wb") as atks:
                pickle.dump(attacks, atks)
            print(f"the value of '{var_name}' for the attack named '{action_name}' was changed to '{new_value}'.")
        else:
            print("no attack with the specified name was set for this character!")
    # spells
    else:
        if hasattr(spells[action_name], var_name):
            setattr(spells[action_name], var_name, new_value)
            with open(f"{config.char_name}/spells_{config.char_name}.pkl", "wb") as spls:
                pickle.dump(spells, spls)
        else:
            print("no spell with the specified name was set for this character!")
    return None

# casts

def katana():
    stat_mod = max(stats_module.str, stats_module.dex)
    hit_cast = cast_module.roll_dice_script(20, 1)[0]
    if hit_cast == 20:
        hit_cast = "nat20"
    elif hit_cast == 1:
        hit_cast = "nat1"
    else:
        hit_cast += stat_mod + stats_module.prf_mod
    dmg_cast_slashing = max(cast_module.roll_dice_script(8, 1), cast_module.roll_dice_script(8, 1))[0] + stats_module.prf_mod
    dmg_cast_radiant = max(cast_module.roll_dice_script(4, 1), cast_module.roll_dice_script(4, 1))[0] + stats_module.prf_mod
    return print(f"hit cast: {hit_cast}, damage cast (slashing): {dmg_cast_slashing}, damage cast (radiant): {dmg_cast_radiant}, damage types: slashing, radiant")

def perform_attack():
    tmp = False
    while not tmp:
        name = input("please enter your attack's name:    ")
        try:
            atk = attacks[name]
            tmp = True
        except:
            print("there is no saved attack with that name...")
    if atk.is_finesse:
        stat_mod = max(stats_module.str, stats_module.dex)
    else:
        stat_mod = stats_module.str
    hit_cast = cast_module.roll_dice_script(20, 1)[0]
    if hit_cast == 20:
        hit_cast = "nat20"
    elif hit_cast == 1:
        hit_cast = "nat1"
    else:
        hit_cast += stat_mod
        if atk.is_proficient:
            hit_cast += stats_module.prf_mod
    dmg_cast = atk.fixed_value
    for i in cast_module.roll_dice_script(atk.die_type, atk.n_dice):
        dmg_cast += i
    if atk.is_proficient:
        dmg_cast += stats_module.prf_mod
    return print(f"hit cast: {hit_cast}, damage cast: {dmg_cast}, damage type: {atk.dmg_type}")

def perform_spell():
    tmp = False
    while not tmp:
        name = input("please enter your spell's name:    ")
        try:
            spell = spells[name]
            tmp = True
        except:
            print("there is no saved spell with that name...")
    # ignore spell slots if spell is a cantrip
    if spell.slot_lv != '0':
        tmp = spell_slots[spell.slot_lv][0]
        if tmp > 0:
            occupy_spell_slot(spell.slot_lv)
            is_wild_magic = wild_magic(False)
        else:
            print("you're out of spell slots for this level!")
            return None
    else:
        is_wild_magic = wild_magic(True)
    if not is_wild_magic:
        dmg_cast = spell.fixed_value
        print(f"fixed_value: {spell.fixed_value}")
        index = 0
        for i in cast_module.roll_dice_script(spell.die_type, spell.n_dice):
            if config.show_calculations:
                print(f"dmg_cast[{index}]: {i}")
                index += 1
            dmg_cast += i
        if spell.needs_hit_cast:
            hit_cast = cast_module.roll_dice_script(20, 1)[0]
            if config.show_calculations:
                print(f"hit roll: {hit_cast}, spellcast_mod: {stats_module.stats[stats_module.spellcast_stat]}, prf_mod: {stats_module.prf_mod}")
            if hit_cast == 20:
                hit_cast = "nat20"
            elif hit_cast == 1:
                hit_cast = "nat1"
            else:
                hit_cast += stats_module.stats[stats_module.spellcast_stat] + stats_module.prf_mod
            return print(f"hit cast: {hit_cast}, damage cast: {dmg_cast}, save type: {spell.save_type}, fixed save: {spell.fixed_save}, spell save dc: {stats_module.spell_save_dc}")
        else:
            return print(f"damage cast: {dmg_cast}, save type: {spell.save_type}, fixed save: {spell.fixed_save}, spell save dc: {stats_module.spell_save_dc}")
    else:
        return None
    
katana()