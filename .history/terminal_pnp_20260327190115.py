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
"stats" to set a stat; -a to set all
"pay" to make a payment
"payday" to add money to the wallet
"ds attacks" to display all attacks
"ds spells" to display all spells
"ds attack info" to display an attack's attributes
"ds spell info" to display a spell's info
"ds spell slots" to display all spell slots
"ds wallet" to display the wallet
"ds artifacts" to display all artifact abilities
"ds artifact info" to display an artifact's attributes
"ds settings" to display all settings
"ds hp" to display current, max and tmp hp
"ds inv" to display the entire inventory
"ds item" to display an item's description
"ds prf" to display all proficiencies
"kat" to use liavyre's katana (liavyre only)
"""

import importlib
import json
from pathlib import Path

dir = Path(__file__).parent
  
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
    print("health has been restored by half max hp!")
    health_module.heal_dmg(health_module.hp_max // 2)
    actions_module.reset_pact_slots()
    artifacts = artifacts_module.artifact_abilities
    for i in artifacts:
        if artifacts[i][2]:
            artifacts[i][0] = artifacts[i][1]
    print("artifact ability cooldowns have been reset!")
    with open(f"{dir}/{config.char_name}/artifacts_{config.char_name}.json", 'w') as file:
            json.dump(artifacts, file, indent = 4)
    return None

def long_rest():
    print("health has been restored completely!")
    health_module.heal_dmg(health_module.hp_max)
    actions_module.reset_spell_slots()
    artifacts = artifacts_module.artifact_abilities
    for i in artifacts:
        artifacts[i][0] = artifacts[i][1]
    print("artifact ability cooldowns have been reset!")
    with open(f"{dir}/{config.char_name}/artifacts_{config.char_name}.json", 'w') as file:
            json.dump(artifacts, file, indent = 4)
    return print("long rest complete!")

def input_loop():
    while True:
        command = input("\nyour turn!    ")
        print("")
        match command:
            case "q":
                print("\nexiting terminal_dnd.py...\n")
                quit()
            case "dice":
                print(f"\ncasts: {cast_module.roll_dice()}")
            case "100":
                tmp = cast_module.probability()
                if tmp:
                    print("\ncast successful!")
                else:
                    print("\ncast failed!")
            case "cast":
                cast_module.cast_on_stat()
            case "dmg":
                health_module.take_dmg()
            case "heal":
                print("")
                health_module.heal_dmg()
            case "tmp":
                health_module.add_tmp_hp()
            case "inv -a":
                inv_module.add_item()
            case "inv -rm":
                inv_module.remove_item()
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
            case "spell -au":
                actions_module.add_unlisted()
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
                        print("all stats have been modified successfully!")
                    case "str":
                        stats_module.set_strn()
                        print("str has been set successfully!")
                    case "dex":
                        stats_module.set_dex()
                        print("dex has been set successfully!")
                    case "con":
                        stats_module.set_con()
                        print("con has been set successfully!")
                    case "int":
                        stats_module.set_intl()
                        print("int has been set successfully!")
                    case "wis":
                        stats_module.set_wis()
                        print("wis has been set successfully!")
                    case "cha":
                        stats_module.set_cha()
                        print("cha has been set successfully!")
                    case "mv":
                        stats_module.set_mv()
                        print("mv has been set successfully!")
                    case "prf":
                        stats_module.set_prf_mod()
                        print("prf mod has been set successfully!")
                    case "prf -a":
                        stats_module.proficiencies_setup()
                        print("all prf mods have been set successfully!")
                    case "spl_stat" | "spellcast_stat":
                        stats_module.set_spellcast_stat()
                        print("spellcasting stat has been set successfully!")
                    case "pact" | "pact_slot_lv":
                        stats_module.set_pact_slot_lv()
                        print("pact slot level has been set successfully!")
                    case default:
                        print("this is not a valid stat!")
                stats_module.update_stats_dict()
                stats_module.save_stats()
            case "pay":
                wallet_module.payment()
            case "payday":
                wallet_module.payday()
            # display functions
            case "ds attacks":
                actions_module.display_actions('a')
            case "ds spells":
                actions_module.display_actions('s')
                actions_module.display_unlisted()
            case "ds actions":
                actions_module.display_actions('b')
            case "ds attack info":
                actions_module.display_action_info('a')
            case "ds spell info":
                actions_module.display_action_info('s')
            case "ds spell slots":
                actions_module.display_spell_slots()
            case "ds wallet":
                wallet_module.display_wallet()
            case "ds artifacts":
                artifacts_module.display_artifacts()
            case "ds artifact info":
                artifacts_module.display_artifact_info()
            case "ds settings":
                config.display_settings()
            case "ds hp":
                health_module.display_health()
            case "ds inv":
                inv_module.display_inventory()
            case "ds item":
                inv_module.display_item()
            case "ds prf":
                prf_module.display_prfs()
            # custom
            case "kat" | "katana":
                actions_module.katana()
            # default
            case default:
                print("\ninvalid command")
        print("---")

def init():
    config.init_settings(dir)
    if config.char_select_on_startup:
        config.char_select()
    health_module.init_health(dir)
    stats_module.init_stats(dir)
    prf_module.init_proficiencies(dir)
    inv_module.init_inventory(dir)
    actions_module.init_actions(dir)
    artifacts_module.init_artifact_abilities(dir)
    wallet_module.init_wallet(dir)
    input_loop()
    return None

init()