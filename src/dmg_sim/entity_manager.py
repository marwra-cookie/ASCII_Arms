from . import *
from .launcher import project_root
from copy import deepcopy
import json
import os


enemies = {}
bosses = {}

base_stats = {
    "info": {"id": None, "name": None, "icon": "🙂", "level": 1, "slain": 0},
    "stats": {
        "attackPower": AttackPower(10),
        "spellPower": SpellPower(10),
        "healingPower": HealingPower(10),
        "criticalChance": CriticalChance(0.1),
        "criticalDamage": CriticalChance(1.5),
        "armorPenetration": ArmorPenetration(0),
        "spellPenetration": SpellPenetration(0),
        "health": Health(500),
        "defense": Defense(0),
        "resistance": Resistance(0),
        "dodge": Dodge(0.1),
        "parry": Parry(0.1),
        "regeneration": Regeneration(0),
        "energy": Energy(3),
        "momentum": Momentum(100),
    },
    "spells": {
        "Slot 1": None,
        "Slot 2": None,
        "Slot 3": None,
        "Slot 4": None,
    },
    "items": {
        "accessory": None,
        "armor": None,
        "boots": None,
        "helm": None,
        "potion": None,
        "weapon": None,
    },
}


def save_player(player):

    profile = deepcopy(player.__dict__)

    json_path = os.path.join(project_root, "database", "entities.json")

    with open(json_path, "r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    found = False

    for i, save in enumerate(data["player"]):
        if profile["info"]["id"] == save["info"]["id"]:
            found = True

            for stat in profile["stats"]:
                profile["stats"][stat] = profile["stats"][stat].value

            for spell in profile["spells"]:
                if profile["spells"][spell] == None:
                    profile["spells"][spell] = None
                else:
                    profile["spells"][spell] = profile["spells"][spell].info["id"]

            for item in profile["items"]:
                if profile["items"][item] == None:
                    profile["items"][item] = None
                else:
                    profile["items"][item] = profile["items"][item].info["id"]

            data["player"][i] = profile
            break

    if found is not True:
        for stat in profile["stats"]:
            profile["stats"][stat] = profile["stats"][stat].value

        for spell in profile["spells"]:
            if profile["spells"][spell] == None:
                profile["spells"][spell] = None
            else:
                profile["spells"][spell] = profile["spells"][spell].info["id"]

        for item in profile["items"]:
            if profile["items"][item] == None:
                profile["items"][item] = None
            else:
                profile["items"][item] = profile["items"][item].info["id"]

        data["player"].append(profile)

    with open(json_path, "w") as write_file:
        json.dump(data, write_file, indent=4)


def load_player(id):

    json_path = os.path.join(project_root, "database", "entities.json")

    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        for player in data["player"]:
            if id == player["info"]["id"]:
                for stat in player["stats"]:
                    match stat:
                        case "attackPower":
                            player["stats"][stat] = AttackPower(player["stats"][stat])
                        case "spellPower":
                            player["stats"][stat] = SpellPower(player["stats"][stat])
                        case "healingPower":
                            player["stats"][stat] = HealingPower(player["stats"][stat])
                        case "criticalChance":
                            player["stats"][stat] = CriticalChance(
                                player["stats"][stat]
                            )
                        case "criticalDamage":
                            player["stats"][stat] = CriticalDamage(
                                player["stats"][stat]
                            )
                        case "armorPenetration":
                            player["stats"][stat] = ArmorPenetration(
                                player["stats"][stat]
                            )
                        case "spellPenetration":
                            player["stats"][stat] = SpellPenetration(
                                player["stats"][stat]
                            )
                        case "energy":
                            player["stats"][stat] = Energy(player["stats"][stat])
                        case "momentum":
                            player["stats"][stat] = Momentum(player["stats"][stat])
                        case "health":
                            player["stats"][stat] = Health(player["stats"][stat])
                        case "defense":
                            player["stats"][stat] = Defense(player["stats"][stat])
                        case "resistance":
                            player["stats"][stat] = Resistance(player["stats"][stat])
                        case "dodge":
                            player["stats"][stat] = Dodge(player["stats"][stat])
                        case "parry":
                            player["stats"][stat] = Parry(player["stats"][stat])
                        case "regeneration":
                            player["stats"][stat] = Regeneration(player["stats"][stat])

                for spell in player["spells"]:
                    player["spells"][spell] = get_spell_id(player["spells"][spell])

                for item in player["items"]:
                    player["items"][item] = get_item_id(player["items"][item])

                return Player(**player)
    return None


def load_enemies():

    json_path = os.path.join(project_root, "database", "entities.json")

    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        for enemy in data["enemy"]:

            for stat in enemy["stats"]:
                match stat:
                    case "attackPower":
                        enemy["stats"][stat] = AttackPower(enemy["stats"][stat])
                    case "spellPower":
                        enemy["stats"][stat] = SpellPower(enemy["stats"][stat])
                    case "healingPower":
                        enemy["stats"][stat] = HealingPower(enemy["stats"][stat])
                    case "criticalChance":
                        enemy["stats"][stat] = CriticalChance(enemy["stats"][stat])
                    case "criticalDamage":
                        enemy["stats"][stat] = CriticalDamage(enemy["stats"][stat])
                    case "armorPenetration":
                        enemy["stats"][stat] = ArmorPenetration(enemy["stats"][stat])
                    case "spellPenetration":
                        enemy["stats"][stat] = SpellPenetration(enemy["stats"][stat])
                    case "energy":
                        enemy["stats"][stat] = Energy(enemy["stats"][stat])
                    case "momentum":
                        enemy["stats"][stat] = Momentum(enemy["stats"][stat])
                    case "health":
                        enemy["stats"][stat] = Health(enemy["stats"][stat])
                    case "defense":
                        enemy["stats"][stat] = Defense(enemy["stats"][stat])
                    case "resistance":
                        enemy["stats"][stat] = Resistance(enemy["stats"][stat])
                    case "dodge":
                        enemy["stats"][stat] = Dodge(enemy["stats"][stat])
                    case "parry":
                        enemy["stats"][stat] = Parry(enemy["stats"][stat])
                    case "regeneration":
                        enemy["stats"][stat] = Regeneration(enemy["stats"][stat])

            enemies[enemy["info"]["id"]] = Enemy(**enemy)

        for boss in data["boss"]:
            for stat in boss["stats"]:
                match stat:
                    case "attackPower":
                        boss["stats"][stat] = AttackPower(boss["stats"][stat])
                    case "spellPower":
                        boss["stats"][stat] = SpellPower(boss["stats"][stat])
                    case "healingPower":
                        boss["stats"][stat] = HealingPower(boss["stats"][stat])
                    case "criticalChance":
                        boss["stats"][stat] = CriticalChance(boss["stats"][stat])
                    case "criticalDamage":
                        boss["stats"][stat] = CriticalDamage(boss["stats"][stat])
                    case "armorPenetration":
                        boss["stats"][stat] = ArmorPenetration(boss["stats"][stat])
                    case "spellPenetration":
                        boss["stats"][stat] = SpellPenetration(boss["stats"][stat])
                    case "energy":
                        boss["stats"][stat] = Energy(boss["stats"][stat])
                    case "momentum":
                        boss["stats"][stat] = Momentum(boss["stats"][stat])
                    case "health":
                        boss["stats"][stat] = Health(boss["stats"][stat])
                    case "defense":
                        boss["stats"][stat] = Defense(boss["stats"][stat])
                    case "resistance":
                        boss["stats"][stat] = Resistance(boss["stats"][stat])
                    case "dodge":
                        boss["stats"][stat] = Dodge(boss["stats"][stat])
                    case "parry":
                        boss["stats"][stat] = Parry(boss["stats"][stat])
                    case "regeneration":
                        boss["stats"][stat] = Regeneration(boss["stats"][stat])

            bosses[boss["info"]["id"]] = Enemy(**boss)


def find_enemy(level, boss_encounter):
    matches = {}

    if boss_encounter:
        for boss in bosses:
            lvl = bosses[boss].info["level"]
            if abs(lvl - level) <= 1:
                matches[boss] = bosses[boss]
    else:
        for enemy in enemies:
            lvl = enemies[enemy].info["level"]
            if abs(lvl - level) <= 1:
                matches[enemy] = enemies[enemy]

    who_to_fight = random.choice(list(matches))
    encounter = matches[who_to_fight]

    return encounter


def get_last_entity_id():
    i = 0

    for enemy in enemies:
        id = enemies[enemy].info["id"]
        if id > i:
            i = id

    return i


def get_enemy_name(name):
    for enemy in enemies:
        if name == enemies[enemy].info["name"]:
            return enemy
    return None


def get_enemy_id(i):
    for enemy in enemies:
        if i == enemies[enemy].info["id"]:
            return enemy

    return None
