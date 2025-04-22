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


def create_random_gear(level):
    gear_types = list(armory.keys())

    slots = len(gear_types) - 1
    slot = gear_types[random.randint(0, slots)]

    gear = create_gear(slot, level)

    return gear


def create_gear(slot, level):

    match slot:
        case "helm":
            helm = Helm(**set_gear_stats(slot, level))
            armory["helm"].append(helm)

            save_gear("helm", helm)
            return helm
        case "armor":
            armor = Armor(**set_gear_stats(slot, level))
            armory["armor"].append(armor)

            save_gear("armor", armor)
            return armor
        case "boots":
            boots = Boots(**set_gear_stats(slot, level))
            armory["boots"].append(boots)

            save_gear("boots", boots)
            return boots
        case "accessory":
            accessory = Accessory(**set_gear_stats(slot, level))
            armory["accessory"].append(accessory)

            save_gear("accessory", accessory)
            return accessory
        case "weapon":
            weapon = Weapon(**set_gear_stats(slot, level))
            armory["weapon"].append(weapon)

            save_gear("weapon", weapon)
            return weapon
    return None


def set_gear_stats(slot, level) -> dict:

    with open(f"database/randomize.json", "r") as file:
        data = json.load(file)
        tier_names = data[slot]
        size = len(tier_names[str(level)])
        name = tier_names[str(level)][random.randint(0, size - 1)]

    match slot:
        case "helm":
            quality = [6, 5, 4, 3, 2]
            base_stats = [
                "health",
                "defense",
                "resistance",
                "attackPower",
                "spellPower",
                "healingPower",
                "energy",
                "momentum",
            ]

            quantity = quality[level - 1]

            while quantity > 0:
                stat = random.randrange(len(base_stats))
                base_stats.pop(stat)
                quantity -= 1

            name = set_identity(name, base_stats)

            stats = {
                "id": get_max_gear_id() + 1,
                "name": name,
                "level": level,
            }

            for stat in base_stats:
                stats[stat] = set_stat(stat, level)

            return stats

        case "armor":
            quality = [4, 4, 3, 2, 1]
            base_stats = [
                "health",
                "defense",
                "resistance",
                "dodge",
                "parry",
                "regeneration",
            ]

            quantity = quality[level - 1]

            while quantity > 0:
                stat = random.randrange(len(base_stats))
                base_stats.pop(stat)
                quantity -= 1

            name = set_identity(name, base_stats)

            stats = {
                "id": get_max_gear_id() + 1,
                "name": name,
                "level": level,
            }

            for stat in base_stats:
                stats[stat] = set_stat(stat, level)

            return stats

        case "boots":
            quality = [2, 2, 1, 1, 0]
            base_stats = [
                "dodge",
                "energy",
                "momentum",
            ]

            quantity = quality[level - 1]

            while quantity > 0:
                stat = random.randrange(len(base_stats))
                base_stats.pop(stat)
                quantity -= 1

            name = set_identity(name, base_stats)

            stats = {
                "id": get_max_gear_id() + 1,
                "name": name,
                "level": level,
            }

            for stat in base_stats:
                stats[stat] = set_stat(stat, level)

            return stats

        case "accessory":
            quality = [7, 6, 5, 4, 3]
            base_stats = [
                "attackPower",
                "spellPower",
                "healingPower",
                "criticalChance",
                "criticalDamage",
                "armorPenetration",
                "spellPenetration",
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

            while quantity > 0:
                stat = random.randrange(len(base_stats))
                base_stats.pop(stat)
                quantity -= 1

            stats = {
                "id": get_max_gear_id() + 1,
                "name": name,
                "level": level,
            }

            for stat in base_stats:
                nr = set_stat(stat, level)
                if int(nr) >= 2:
                    nr = int(nr / 3)

                if nr > 0:
                    stats[stat] = nr

            return stats

        case "weapon":
            weapon_types = [
                "Sword",
                "Dagger",
                "Mace",
                "Axe",
                "Bow",
                "Crossbow",
                "Staff",
                "Scythe",
                "Wand",
            ]

            size = len(weapon_types) - 1
            weapon = weapon_types[random.randint(0, size)]

            base_stats = set_weapon_stats(weapon)

            quality = [4, 3, 2, 1, 0]
            quantity = quality[level - 1]

            while quantity > 0:
                stat = random.randrange(len(base_stats))
                base_stats.pop(stat)
                quantity -= 1

            name = set_identity(f"{name} {weapon}", base_stats)

            stats = {
                "id": get_max_gear_id() + 1,
                "name": name,
                "level": level,
            }

            for stat in base_stats:
                stats[stat] = set_stat(stat, level)

            return stats
    return {}


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
        case "armorPenetration":
            return set_armor_penetration(level)
        case "spellPenetration":
            return set_spell_penetration(level)
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


def set_weapon_stats(name) -> list:
    match name:
        case "Sword":
            base_stats = [
                "attackPower",
                "armorPenetration",
                "criticalChance",
                "energy",
                "parry",
            ]

            return base_stats
        case "Dagger":
            base_stats = [
                "attackPower",
                "armorPenetration",
                "criticalDamage",
                "momentum",
                "parry",
            ]

            return base_stats
        case "Mace":
            base_stats = [
                "attackPower",
                "armorPenetration",
                "criticalDamage",
                "energy",
                "parry",
            ]

            return base_stats

        case "Axe":
            base_stats = [
                "attackPower",
                "armorPenetration",
                "criticalDamage",
                "energy",
                "parry",
            ]

            return base_stats

        case "Bow":
            base_stats = [
                "attackPower",
                "armorPenetration",
                "criticalChance",
                "energy",
                "momentum",
            ]

            return base_stats
        case "Crossbow":
            base_stats = [
                "attackPower",
                "armorPenetration",
                "criticalDamage",
                "energy",
                "momentum",
            ]

            return base_stats
        case "Staff":
            base_stats = [
                "spellPower",
                "healingPower",
                "spellPenetration",
                "criticalDamage",
                "energy",
            ]

            return base_stats
        case "Scythe":
            base_stats = [
                "spellPower",
                "healingPower",
                "spellPenetration",
                "criticalDamage",
                "energy",
                "parry",
            ]

            return base_stats
        case "Wand":
            base_stats = [
                "spellPower",
                "healingPower",
                "spellPenetration",
                "criticalChance",
                "momentum",
            ]

            return base_stats
    return []


def set_identity(name, stats):
    with open(f"database/randomize.json", "r") as file:
        data = json.load(file)
        identities = data["identity"]

    for stat in stats:
        name += identities[stat]
        break

    return name


def set_attack_power(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_spell_power(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_healing_power(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_armor_penetration(level) -> float:
    stat = (random.randint(1, 5) * level) / 100

    return stat


def set_spell_penetration(level) -> float:
    stat = (random.randint(1, 5) * level) / 100

    return stat


def set_critical_chance(level) -> float:
    stat = (random.randint(1, 5) * level) / 100

    return stat


def set_critical_damage(level) -> float:
    stat = (random.randint(1, 5) * level) / 100

    return stat


def set_health(level) -> int:
    stat = random.randint(1, 200) * level

    return stat


def set_defense(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_resistance(level) -> int:
    stat = random.randint(1, 20) * level

    return stat


def set_parry(level) -> float:
    stat = (random.randint(1, 5) * level) / 100

    return stat


def set_dodge(level) -> float:
    stat = (random.randint(1, 5) * level) / 100

    return stat


def set_regeneration(level) -> float:
    stat = (random.randint(1, 5) * level) / 100

    return stat


def set_energy() -> int:
    stat = random.randint(1, 4)

    return stat


def set_momentum(level) -> int:
    stat = random.randint(1, 10) * level

    return stat


def save_gear(slot, gear):
    with open(f"database/gear.json", "r+") as file:
        data = json.load(file)
        data[slot].append(gear.__dict__)
        file.seek(0)
        json.dump(data, file, indent=4)


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


def get_max_gear_id():
    i = 0

    for category in armory:
        for item in armory[category]:
            if item.id > i:
                i = item.id

    return i


def get_gear(name):
    for slot in armory:
        if len(slot) != None:
            for item in armory[slot]:
                if item.name == name:
                    return item
    return None


def get_max_spell_id():
    i = 0

    for category in spellbook:
        for spell in spellbook[category]:
            if spell.id > i:
                i = spell.id

    return i


def get_spell(name):
    for category in spellbook:
        for item in spellbook[category]:
            if item.name == name:
                return item
    return None
