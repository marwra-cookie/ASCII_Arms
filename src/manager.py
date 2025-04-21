import json
import random
from src.graphics import *
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
    "weapon": [],
}

spellbook = {"direct": [], "passive": []}


def testbench():
    debug = create_gear(1)

    print(red(f"\n\nDEBUG: {debug}"))


def create_gear(level):
    gear_types = list(armory.keys())

    slots = len(gear_types) - 1
    slot = gear_types[random.randint(0, slots)]

    match slot:
        case "helm":
            helm = Helm(**set_gear_stats(slot, level))
            armory["helm"].append(helm)

            return helm
        case "armor":
            armor = Armor(**set_gear_stats(slot, level))
            armory["armor"].append(armor)

            return armor
        case "boots":
            boots = Boots(**set_gear_stats(slot, level))
            armory["boots"].append(boots)

            return boots
        case "accessory":
            accessory = Accessory(**set_gear_stats(slot, level))
            armory["accessory"].append(accessory)

            return accessory
        case "weapon":
            weapon = Weapon(**set_gear_stats(slot, level))
            armory["weapon"].append(weapon)

            return weapon
    return None


def set_gear_stats(slot, level):

    with open(f"database/randomize.json", "r") as file:
        data = json.load(file)
        tier_names = data[slot]
        size = len(tier_names[str(level)])
        name = tier_names[str(level)][random.randint(0, size - 1)]

    match slot:
        case "helm":
            quality = [2, 3, 4, 5, 6]
            stats = [
                "attackPower",
                "spellPower",
                "healingPower",
                "energy",
                "momentum",
                "health",
                "defense",
                "resistance",
            ]

            quantity = quality[level - 1]
            set_stats = random.sample(stats, quantity)
            stats = {
                "name": name,
                "lvl": level,
            }

            for stat in set_stats:
                stats[stat] = set_stat(stat, level)

            return stats

        case "armor":
            quality = [1, 2, 3, 4, 5]
            stats = [
                "health",
                "defense",
                "resistance",
                "dodge",
                "parry",
                "regeneration",
            ]

            quantity = quality[level - 1]
            set_stats = random.sample(stats, quantity)
            stats = {
                "name": name,
                "lvl": level,
            }

            for stat in set_stats:
                stats[stat] = set_stat(stat, level)

            return stats

        case "boots":
            quality = [1, 1, 2, 2, 3]
            stats = [
                "dodge",
                "energy",
                "momentum",
            ]

            quantity = quality[level - 1]
            set_stats = random.sample(stats, quantity)
            stats = {
                "name": name,
                "lvl": level,
            }

            for stat in set_stats:
                stats[stat] = set_stat(stat, level)

            return stats

        case "accessory":
            quality = [3, 4, 5, 6, 7]
            stats = [
                "attackPower",
                "spellPower",
                "healingPower",
                "criticalChance",
                "criticalDamage",
                "energy",
                "momentum",
                "health",
                "defense",
                "resistance",
                "dodge",
                "parry",
                "regeneration",
            ]

            quantity = quality[level - 1]
            set_stats = random.sample(stats, quantity)
            stats = {
                "name": name,
                "lvl": level,
            }

            for stat in set_stats:
                stats[stat] = set_stat(stat, level)

            return stats

        case "weapon":
            weapon_types = [
                "Sword",
                "Dagger",
                "Mace",
                "Staff",
                "Axe",
                "Spear",
                "Bow",
                "Crossbow",
                "Hammer",
                "Katana",
                "Rapier",
                "Flail",
                "Scythe",
                "Wand",
            ]

            size = len(weapon_types) - 1
            weapon = weapon_types[random.randint(0, size)]

            stats = [
                "attackPower",
                "spellPower",
                "healingPower",
                "criticalChance",
                "criticalDamage",
                "energy",
                "momentum",
                "parry",
            ]

            quality = [2, 3, 4, 5, 6]
            quantity = quality[level - 1]
            set_stats = random.sample(stats, quantity)
            stats = {
                "name": f"{name} {weapon}",
                "lvl": level,
            }

            for stat in set_stats:
                stats[stat] = set_stat(stat, level)

            return stats
    return None


def set_stat(stat, level):
    match stat:
        case "attackPower":
            return set_attack_power(level)
        case "spellPower":
            return set_spell_power(level)
        case "healingPower":
            return set_healing_power(level)
        case "criticalChance":
            return set_critical_chance(level)
        case "criticalDamage":
            return set_critical_damage(level)
        case "energy":
            return set_energy()
        case "momentum":
            return set_momentum(level)
        case "health":
            return set_health(level)
        case "defense":
            return set_defense(level)
        case "resistance":
            return set_resistance(level)
        case "dodge":
            return set_dodge(level)
        case "parry":
            return set_parry(level)
        case "regeneration":
            return set_regeneration(level)
    return None


def set_attack_power(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_spell_power(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_healing_power(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_critical_chance(level) -> float:
    stat = (random.randint(1, 20) * level) / 100

    return stat


def set_critical_damage(level) -> float:
    stat = (random.randint(1, 20) * level) / 100

    return stat


def set_health(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_defense(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_resistance(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_parry(level) -> float:
    stat = (random.randint(1, 20) * level) / 100

    return stat


def set_dodge(level) -> float:
    stat = (random.randint(1, 20) * level) / 100

    return stat


def set_regeneration(level) -> float:
    stat = (random.randint(1, 20) * level) / 100

    return stat


def set_energy() -> int:
    stat = random.randint(1, 4)

    return stat


def set_momentum(level) -> int:
    stat = random.randint(1, 10) * level

    return stat


def load_gear():
    gear_types = list(armory.keys())

    with open(f"database/gear.json", "r") as file:
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

    with open(f"database/spells.json", "r") as file:
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
