### arguments to call specific functions ###
"""
"dice" to roll n [die]-sided dice
"100" to make a cast of [percent] percent probability
"cast" to make a cast on a specified stat
"dmg" to make char take [dmg] points of damage
"heal" to heal [heal] points of damage
"tmp" to add temp hp
"inv -a" to append an item to inventory
"inv -rm" to remove an item from from inventory
"act -a" to add an action
"act -rm" to remove an action
"act -mod" to modify an action
"atk" to perform an attack
"spell" to perform a spell
"spell -u" to perform a spell not listed as an action; only for spells that don't require casts by the caster's player
"slots" to modify max spell slots
"artifacts -a" to add artifact abilities
"artifacts -rm" to remove artifact abilities
"rest -s" or "short rest" to make a short rest
"rest -l" or "long rest" to make a long rest
"kat" to use liavyre's katana (liavyre only)
"""

import importlib
import json
# to be implemented: choose a specific char's config file
# set char_name and stats in config.py
  
config = importlib.import_module("config")
cast_module = importlib.import_module("casts")
health_module = importlib.import_module("health")
stats_module = importlib.import_module("stats")
prf_module = importlib.import_module("proficiencies")
inv_module = importlib.import_module("inventory")
actions_module = importlib.import_module("actions")
artifacts_module = importlib.import_module("artifacts")
wallet_module = importlib.import_module("wallet")

def short_rest():
    health_module.heal_dmg(health_module.hp_max // 2)
    actions_module.reset_pact_slots()
    artifacts = artifacts_module.artifact_abilities
    for i in artifacts:
        if artifacts[i][2]:
            artifacts[i][0] = artifacts[i][1]
    with open(f"{config.char_name}/artifacts_{config.char_name}.json", 'w') as file:
            json.dump(artifacts, file, indent = 4)
    return print("short rest complete!")

def long_rest():
    health_module.heal_dmg(health_module.hp_max)
    actions_module.reset_spell_slots()
    artifacts = artifacts_module.artifact_abilities
    for i in artifacts:
        artifacts[i][0] = artifacts[i][1]
    with open(f"{config.char_name}/artifacts_{config.char_name}.json", 'w') as file:
            json.dump(artifacts, file, indent = 4)
    return print("long rest complete!")

def input_loop():
    while True:
        command = input("your turn!    ")
        match command:
            case "q":
                print("exiting terminal_dnd.py...")
                quit()
            case "dice":
                cast_module.roll_dice()
            case "100":
                cast_module.probability()
            case "cast":
                cast_module.cast_on_stat()
            case "dmg":
                health_module.take_dmg()
            case "heal":
                health_module.heal_dmg()
            case "tmp":
                health_module.add_tmp_hp()
            case "inv -a":
                inv_module.add_item()
            case "inv -rm":
                inv_module.rm_item()
            case "act -a":
                actions_module.add_action()
            case "act -rm":
                actions_module.rm_action()
            case "act -mod":
                actions_module.mod_action()
            case "atk":
                actions_module.perform_attack()
            case "spell":
                actions_module.perform_spell()
            case "spell -u":
                actions_module.cast_unlisted_spell()
            case "slots":
                actions_module.mod_max_spell_slots()
            case "artifacts -a":
                artifacts_module.add_artifact_ability()
            case "artifacts -rm":
                artifacts_module.remove_artifact_ability()
            case "rest -s" | "short rest":
                short_rest()
            case "rest -l" | "long rest":
                long_rest()
            case "stats":
                com = input("which stat do you wish to modify? enter '-a' to set them all anew.    ")
                match com:
                    case "-a":
                        stats_module.stat_setup()
                    case "str":
                        stats_module.set_strn()
                    case "dex":
                        stats_module.set_dex()
                    case "con":
                        stats_module.set_con()
                    case "int":
                        stats_module.set_intl()
                    case "wis":
                        stats_module.set_wis()
                    case "cha":
                        stats_module.set_cha()
                    case "mv":
                        stats_module.set_mv()
                    case "prf":
                        stats_module.set_prf_mod()
                    case "prf -a":
                        stats_module.proficiencies_setup()
                    case "spl_stat" | "spellcast_stat":
                        stats_module.set_spellcast_stat()
                    case "pact" | "pact_slot_lv":
                        stats_module.set_pact_slot_lv()
                    case default:
                        print("this is not a valid stat!")
                stats_module.update_stats_dict()
                stats_module.save_stats()
            case "pay":
                wallet_module.payment()
            case "payday":
                wallet_module.payday()
            # custom
            case "kat" | "katana":
                actions_module.katana()
            # default
            case default:
                print("invalid command")

def init():
    config.init_settings()
    if config.char_select_on_startup:
        config.char_select()
    health_module.init_health()
    stats_module.init_stats()
    prf_module.init_proficiencies()
    inv_module.init_inventory()
    actions_module.init_actions()
    artifacts_module.init_artifact_abilities()
    wallet_module.init_wallet()
    input_loop()
    return None

init()