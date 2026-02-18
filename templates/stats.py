# enter stat mods
str = 0
dex = 0
con = 0
int = 0
wis = 0
cha = 0
mv = 30
prf_mod = 0
spellcast_stat = "n/a"
pact_slot_lv = "n/a"

### don't touch below here ###

"""below part is outdated; copy from stats_liavyre.py once done"""

# dict for import
stats = {
    "str": str,
    "dex": dex,
    "con": con,
    "int": int,
    "wis": wis,
    "cha": cha,
    "initiative": dex,
    "str_save": str,
    "dex_save": dex,
    "con_save": con,
    "int_save": int,
    "wis_save": wis,
    "cha_save": cha,
    "acrobatics": dex,
    "animal_handling": wis,
    "arcana": int,
    "athletics": str,
    "deception": cha,
    "history": int,
    "insight": wis,
    "intimidation": cha,
    "investigation": int,
    "medicine": wis,
    "nature": wis,
    "perception": wis,
    "performance": cha,
    "persuasion": cha,
    "religion": int,
    "sleight_of_hand": dex,
    "stealth": dex,
    "survival": wis
}

def get_stat(stat):
    return stats[stat] + prf_mod * prf[stat]