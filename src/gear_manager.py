import json
import random

from oop import *

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

            base_stats = {
                "health": None,
                "defense": None,
                "resistance": None,
                "attackPower": None,
                "spellPower": None,
                "healingPower": None,
                "energy": None,
                "momentum": None,
            }

            quantity = quality[level - 1]

            while quantity > 0:
                stat = random.randrange(len(base_stats))
                base_stats.pop(stat)
                quantity -= 1

            name = set_identity(name, base_stats)

            stats = {
                "base": {"id": get_max_gear_id() + 1, "name": name, "level": level},
                "stats": {},
            }

            for stat in base_stats:
                stats["stats"][stat] = set_stat(stat, level)

            return stats

        case "armor":
            quality = [4, 4, 3, 2, 1]
            base_stats = {
                "health": None,
                "defense": None,
                "resistance": None,
                "dodge": None,
                "parry": None,
                "regeneration": None,
            }

            quantity = quality[level - 1]

            while quantity > 0:
                stat = random.randrange(len(base_stats))
                base_stats.pop(stat)
                quantity -= 1

            name = set_identity(name, base_stats)

            stats = {
                "base": {"id": get_max_gear_id() + 1, "name": name, "level": level},
                "stats": {},
            }

            for stat in base_stats:
                stats["stats"][stat] = set_stat(stat, level)

            return stats

        case "boots":
            quality = [2, 2, 1, 1, 0]
            base_stats = {
                "dodge": None,
                "energy": None,
                "momentum": None,
            }

            quantity = quality[level - 1]

            while quantity > 0:
                stat = random.randrange(len(base_stats))
                base_stats.pop(stat)
                quantity -= 1

            name = set_identity(name, base_stats)

            stats = {
                "base": {"id": get_max_gear_id() + 1, "name": name, "level": level},
                "stats": {},
            }

            for stat in base_stats:
                stats["stats"][stat] = set_stat(stat, level)

            return stats

        case "accessory":
            quality = [7, 6, 5, 4, 3]
            base_stats = {
                "attackPower": None,
                "spellPower": None,
                "healingPower": None,
                "criticalChance": None,
                "criticalDamage": None,
                "armorPenetration": None,
                "spellPenetration": None,
                "energy": None,
                "momentum": None,
                "health": None,
                "defense": None,
                "resistance": None,
                "dodge": None,
                "parry": None,
                "regeneration": None,
            }

            quantity = quality[level - 1]

            while quantity > 0:
                stat = random.randrange(len(base_stats))
                base_stats.pop(stat)
                quantity -= 1

            stats = {
                "base": {"id": get_max_gear_id() + 1, "name": name, "level": level},
                "stats": {},
            }

            for stat in base_stats:
                nr = set_stat(stat, level)
                if int(nr) >= 2:
                    nr = int(nr / 3)

                if nr > 0:
                    stats["stats"][stat] = set_stat(stat, level)

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
                "base": {"id": get_max_gear_id() + 1, "name": name, "level": level},
                "stats": {},
            }

            for stat in base_stats:
                stats["stats"][stat] = set_stat(stat, level)

            return stats
    return {}


def set_stat(name, level):
    match name:
        case "attackPower":
            return AttackPower(set_attack_power(level))
        case "spellPower":
            return SpellPower(set_spell_power(level))
        case "healingPower":
            return HealingPower(set_healing_power(level))
        case "criticalChance":
            return CriticalChance(set_critical_chance(level))
        case "criticalDamage":
            return CriticalDamage(set_critical_damage(level))
        case "armorPenetration":
            return ArmorPenetration(set_armor_penetration(level))
        case "spellPenetration":
            return SpellPenetration(set_spell_penetration(level))
        case "energy":
            return Energy(set_energy())
        case "momentum":
            return Momentum(set_momentum(level))
        case "health":
            return Health(set_health(level))
        case "defense":
            return Defense(set_defense(level))
        case "resistance":
            return Resistance(set_resistance(level))
        case "dodge":
            return Dodge(set_dodge(level))
        case "parry":
            return Parry(set_parry(level))
        case "regeneration":
            return Regeneration(set_regeneration(level))
    return None


def set_weapon_stats(name) -> list:
    match name:
        case "Sword":
            base_stats = {
                "attackPower": None,
                "armorPenetration": None,
                "criticalChance": None,
                "energy": None,
                "parry": None,
            }

            return base_stats
        case "Dagger":
            base_stats = {
                "attackPower": None,
                "armorPenetration": None,
                "criticalDamage": None,
                "momentum": None,
                "parry": None,
            }

            return base_stats
        case "Mace":
            base_stats = {
                "attackPower": None,
                "armorPenetration": None,
                "criticalDamage": None,
                "energy": None,
                "parry": None,
            }

            return base_stats

        case "Axe":
            base_stats = {
                "attackPower": None,
                "armorPenetration": None,
                "criticalDamage": None,
                "energy": None,
                "parry": None,
            }

            return base_stats

        case "Bow":
            base_stats = {
                "attackPower": None,
                "armorPenetration": None,
                "criticalChance": None,
                "energy": None,
                "momentum": None,
            }

            return base_stats
        case "Crossbow":
            base_stats = {
                "attackPower": None,
                "armorPenetration": None,
                "criticalDamage": None,
                "energy": None,
                "momentum": None,
            }

            return base_stats
        case "Staff":
            base_stats = {
                "spellPower": None,
                "healingPower": None,
                "spellPenetration": None,
                "criticalDamage": None,
                "energy": None,
            }

            return base_stats
        case "Scythe":
            base_stats = {
                "spellPower": None,
                "healingPower": None,
                "spellPenetration": None,
                "criticalDamage": None,
                "energy": None,
                "parry": None,
            }

            return base_stats
        case "Wand":
            base_stats = {
                "spellPower": None,
                "healingPower": None,
                "spellPenetration": None,
                "criticalChance": None,
                "momentum": None,
            }

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
    """"""

    gear_types = list(armory.keys())

    with open(f"database/gear.json", "r") as file:
        data = json.load(file)

        for g in gear_types:
            for item in data[g]:

                for stat in item["stats"]:
                    match stat:
                        case "attackPower":
                            item["stats"][stat] = AttackPower(item["stats"][stat])
                        case "spellPower":
                            item["stats"][stat] = SpellPower(item["stats"][stat])
                        case "healingPower":
                            item["stats"][stat] = HealingPower(item["stats"][stat])
                        case "criticalChance":
                            item["stats"][stat] = CriticalChance(item["stats"][stat])
                        case "criticalDamage":
                            item["stats"][stat] = CriticalDamage(item["stats"][stat])
                        case "armorPenetration":
                            item["stats"][stat] = ArmorPenetration(item["stats"][stat])
                        case "spellPenetration":
                            item["stats"][stat] = SpellPenetration(item["stats"][stat])
                        case "energy":
                            item["stats"][stat] = Energy(item["stats"][stat])
                        case "momentum":
                            item["stats"][stat] = Momentum(item["stats"][stat])
                        case "health":
                            item["stats"][stat] = Health(item["stats"][stat])
                        case "defense":
                            item["stats"][stat] = Defense(item["stats"][stat])
                        case "resistance":
                            item["stats"][stat] = Resistance(item["stats"][stat])
                        case "dodge":
                            item["stats"][stat] = Dodge(item["stats"][stat])
                        case "parry":
                            item["stats"][stat] = Parry(item["stats"][stat])
                        case "regeneration":
                            item["stats"][stat] = Regeneration(item["stats"][stat])
                print(type(item))
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
        for item in armory[slot]:
            if item.base["name"] == name:
                return item
    return None


def get_gear_id(i):
    for slot in armory:
        for item in armory[slot]:
            if item.base["id"] == i:
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


def get_spell_id(i):
    for category in spellbook:
        for item in spellbook[category]:
            if item.id == i:
                return item
    return None
