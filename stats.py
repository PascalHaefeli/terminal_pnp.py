# default stat mods; will be overridden
strn = 0
dex = 0
con = 0
intl = 0
wis = 0
cha = 0
mv = 30
prf_mod = 3
spellcast_stat = "cha"
pact_slot_lv = "0"

### don't touch below here ###

import importlib
import pickle
config = importlib.import_module("config")
prf_module = importlib.import_module(f"proficiencies")

dir = ""

# dicts for export
stats = {
    "str": strn,
    "dex": dex,
    "con": con,
    "int": intl,
    "wis": wis,
    "cha": cha,
    "initiative": dex,
    "str_save": strn,
    "dex_save": dex,
    "con_save": con,
    "int_save": intl,
    "wis_save": wis,
    "cha_save": cha,
    "acrobatics": dex,
    "animal_handling": wis,
    "arcana": intl,
    "athletics": strn,
    "deception": cha,
    "history": intl,
    "insight": wis,
    "intimidation": cha,
    "investigation": intl,
    "medicine": wis,
    "nature": wis,
    "perception": wis,
    "performance": cha,
    "persuasion": cha,
    "religion": intl,
    "sleight_of_hand": dex,
    "stealth": dex,
    "survival": wis,
    "mv" : mv,
    "prf_mod": prf_mod,
    "spellcast_stat" : spellcast_stat,
    "pact_slot_lv" : pact_slot_lv
}

passives = {
    "pas_perception": stats["perception"] + 10,
    "pas_investigation": stats["investigation"] + 10,
    "pas_insight": stats["insight"] + 10
}

spell_save_dc = stats[spellcast_stat] + prf_mod + 8

def get_stat(stat):
    if stat[:4] != "pas_":
        return stats[stat] + prf_mod * prf_module.prf[stat]
    else:
        return passives[stat]

# save and load pickles

def load_stats():
    global stats, strn, dex, con, intl, wis, cha, mv, prf_mod, spellcast_stat, pact_slot_lv
    try:
        with open(f"{dir}/{config.char_name}/stats_{config.char_name}.pkl", 'rb') as file:
            stats = pickle.load(file)
    except:
        return create_stats_file()
    strn = stats["str"]
    dex = stats["dex"]
    con = stats["con"]
    intl = stats["int"]
    wis = stats["wis"]
    cha = stats["cha"]
    mv = stats["mv"]
    prf_mod = stats["prf_mod"]
    spellcast_stat = stats["spellcast_stat"]
    pact_slot_lv = stats["pact_slot_lv"]
    return None

def save_stats():
    with open(f"{dir}/{config.char_name}/stats_{config.char_name}.pkl", 'wb') as file:
        pickle.dump(stats, file)
    return None

### stat setup functions ###

def set_strn():
    global strn
    strn = input("str:    ")
    try:
        strn = int(strn)
    except:
        print("your str needs to be of type integer!")
        return set_strn()
    return strn

def set_dex():
    global dex
    dex = input("dex:    ")
    try:
        dex = int(dex)
    except:
        print("your dex needs to be of type integer!")
        return set_dex()
    return dex

def set_con():
    global con
    con = input("con:    ")
    try:
        con = int(con)
    except:
        print("your con needs to be of type integer!")
        return set_con()
    return con

def set_intl():
    global intl
    intl = input("intl:    ")
    try:
        intl = int(intl)
    except:
        print("your intl needs to be of type integer!")
        return set_intl()
    return intl

def set_wis():
    global wis
    wis = input("wis:    ")
    try:
        wis = int(wis)
    except:
        print("your wis needs to be of type integer!")
        return set_wis()
    return wis

def set_cha():
    global cha
    cha = input("cha:    ")
    try:
        cha = int(cha)
    except:
        print("your cha needs to be of type integer!")
        return set_cha()
    return cha

def set_mv():
    global mv
    mv = input("mv:    ")
    try:
        mv = int(mv)
    except:
        print("your mv needs to be of type integer!")
        return set_mv()
    return mv

def set_prf_mod():
    global prf_mod
    prf_mod = input("prf_mod:    ")
    try:
        prf_mod = int(prf_mod)
    except:
        print("your prf_mod needs to be of type integer!")
        return set_prf_mod()
    return prf_mod

def set_spellcast_stat():
    global spellcast_stat
    spellcast_stat = input("spellcast_stat:    ")
    if not spellcast_stat in stats:
        print(f"{spellcast_stat} is not a valid stat!")
        return set_spellcast_stat()
    return spellcast_stat

def set_pact_slot_lv():
    global pact_slot_lv
    pact_slot_lv = input("pact_slot_lv:    ")
    try:
        if not (0 < int(pact_slot_lv) <= 9):
            print("your pact slot level needs to be in between 1 and 9!")
            return set_pact_slot_lv()
    except:
        print("your pact slot level needs to be of type integer!")
        return set_pact_slot_lv()
    return pact_slot_lv

def update_stats_dict():
    global stats
    stats["str"] = strn
    stats["dex"] = dex
    stats["con"] = con
    stats["int"] = intl
    stats["wis"] = wis
    stats["cha"] = cha
    stats["mv"] = mv
    stats["prf_mod"] = prf_mod
    stats["spellcast_stat"] = spellcast_stat
    stats["pact_slot_lv"] = pact_slot_lv
    return None

setters = [set_strn, set_dex, set_con, set_intl, set_wis, set_cha, set_mv, set_prf_mod, set_spellcast_stat, set_pact_slot_lv]

def stat_setup():
    for function in setters:
        function()
    update_stats_dict()
    return None

def create_stats_file():
    print(f"no file with stats for {config.char_name} was found. initiating stat setup...")
    stat_setup()
    with open(f"{dir}/{config.char_name}/stats_{config.char_name}.pkl", 'xb') as file:
        pickle.dump(stats, file)
    return None

def init_stats(module_dir):
    global dir
    dir = module_dir
    load_stats()
    return None

