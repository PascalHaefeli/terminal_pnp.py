# enter stat mods
str = -1
dex = 3
con = 0
int = 0
wis = 1
cha = 3
mv = 30
prf_mod = 3
spellcast_stat = "cha"
pact_slot_lv = "3"


### don't touch below here ###
import importlib
config = importlib.import_module("config")
prf_module = importlib.import_module(f"{config.char_name}.proficiencies_{config.char_name}")

# dict for export
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
    "survival": wis,
}

passives = {
    "pas_perception": stats["perception"] + 10,
    "pas_investigation": stats["investigation"] + 10,
    "pas_insight": stats["insight"] + 10
}

spell_save_dc = stats[spellcast_stat] + prf_mod + 8

def get_stat(stat):
    if stat[:4] == "pas_":
        return stats[stat] + prf_mod * prf_module.prf[stat]
    else:
        return passives[stat]