import json
import random
from src.loadout.gear.accessory import Accessory
from src.loadout.gear.armor import Armor
from src.loadout.gear.boots import Boots
from src.loadout.gear.gear import Gear
from src.loadout.gear.helm import Helm
from src.loadout.gear.potion import Potion
from src.loadout.gear.weapon import Weapon
from src.loadout.spells.direct import Direct
from src.loadout.spells.passive import Passive
from src.loadout.spells.spells import Spells

error = "Invalid option... Please try again!"

armory = {
    "accessory": [],
    "armor": [],
    "boots": [],
    "helm": [],
    "potion": [],
    "weapon": [],
}

spellbook = {
    "direct": [],
    "passive": []
}

def testbench():
    print("\n\nDEBUG:")
    create_gear(1)

def create_gear(level):
    gear_types = list(armory.keys())

    slots = len(gear_types) - 1
    slot = gear_types[random.randint(0, slots)]

    stats = set_stats(slot, level)

    match slot:
        case "helm":
            helm = Helm(stats)
            armory["helm"].append(helm)
        case "armor":
            armor = Armor(stats)
            armory["armor"].append(armor)
        case "boots":
            boots = Boots(stats)
            armory["boots"].append(boots)
        case "accessory":
            accessory = Accessory(stats)
            armory["accessory"].append(accessory)
        case "weapon":
            weapon = Weapon(stats)
            armory["weapon"].append(weapon)
        case "potion":
            potion = Potion(stats)
            armory["potion"].append(potion)

def set_stats(slot, level):
    stats = {
        "name": "Lesser pendant",
        "lvl": level,
        "attackPower": 1,
        "spellPower": 1,
        "healingPower": 1,
        "criticalChance": None,
        "criticalDamage": None,
        "energy": None,
        "momentum": 5,
        "health": 1,
        "defense": 1,
        "resistance": 1,
        "dodge": 0.05,
        "parry": 0.05,
        "regeneration": 0.05
    }

    match slot:
        case "helm":
            print()
        case "armor":
            print()
        case "boots":
            print()
        case "accessory":
            print()
        case "weapon":
            weapon_types = [
                "Sword", "Dagger", "Mace", "Staff", "Axe", "Spear", "Bow",
                "Crossbow", "Hammer", "Katana", "Rapier", "Flail", "Scythe", "Wand"
            ]
 
            print()
        case "potion":
            print()

    return stats

def load_gear():
    gear_types = list(armory.keys())

    with open(f"database/gear.json") as file:
        data = json.load(file)

        for g in gear_types:
            for item in data[g]:
                match g:
                    case "accessory":
                        armory[g].append(Accessory(**item))
                    case "armor":
                        armory[g].append(Armor(**item))
                    case "boots":
                        armory[g].append(Boots(**item))
                    case "helm":
                        armory[g].append(Helm(**item))
                    case "potion":
                        armory[g].append(Potion(**item))
                    case "weapon":
                        armory[g].append(Weapon(**item))

def load_spells():
    spell_type = list(spellbook.keys())

    with open(f"database/spells.json") as file:
        data = json.load(file)

        for s in spell_type:
            for spell in data[s]:
                if s == "direct":
                    spellbook[s].append(Direct(**spell))
                elif s == "passive":
                    spellbook[s].append(Passive(**spell))

def get_gear(name):
    for slot in armory:
        for item in armory[slot]:
            if item.name == name:
               return item

def get_spell(name):
    for category in spellbook:
        for item in spellbook[category]:
            if item.name == name:
               return item