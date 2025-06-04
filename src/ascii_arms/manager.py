from . import *
from .launcher import project_root
import random
import json
import os


entity_path = os.path.join(project_root, "database", "entities.json")
item_path = os.path.join(project_root, "database", "items.json")
spell_path = os.path.join(project_root, "database", "spells.json")


players = {}
enemies = {}
bosses = {}
armory = {}
spellbook = {"direct": {}, "passive": {}}


# region Entity Manager
base_stats = {
    "info": {"id": None, "name": None, "icon": "🙂", "level": 1, "xp": 0},
    "stats": {
        "attack_power": AttackPower(10),
        "spell_power": SpellPower(10),
        "critical_chance": CriticalChance(0.1),
        "critical_damage": CriticalChance(1.5),
        "penetration": Penetration(0),
        "health": Health(500),
        "mana": Mana(250),
        "defense": Defense(25),
        "resistance": Resistance(25),
        "dodge": Dodge(0.1),
        "life_steal": LifeSteal(0),
        "momentum": Momentum(100),
    },
    "spells": {
        "1": None,
        "2": None,
        "3": None,
        "4": None,
    },
    "items": {
        "helmet": None,
        "armor": None,
        "boots": None,
        "weapon": None,
        "accessory": None,
    },
    "kills": {"enemies": 0, "bosses": 0, "slain": 0},
}


def save_player(player):
    """

    :param player:
    """
    p = deepcopy(player)
    profile = {}
    profile["info"] = p.info
    profile["stats"] = p.stats
    profile["spells"] = p.spells
    profile["items"] = p.items
    profile["kills"] = p.kills

    print(profile)
    for stat in profile["stats"]:
        profile["stats"][stat] = profile["stats"][stat].value

    for spell in profile["spells"]:
        if profile["spells"][spell] is None:
            profile["spells"][spell] = None
        else:
            profile["spells"][spell] = profile["spells"][spell].info["id"]

    for item in profile["items"]:
        if profile["items"][item] is None:
            profile["items"][item] = None
        else:
            profile["items"][item] = profile["items"][item].info["id"]

    for kill in profile["kills"]:
        profile["kills"][kill] = profile["kills"][kill]

    with open(entity_path, "r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    for i, save in enumerate(data["player"]):
        if save["info"]["id"] == profile["info"]["id"]:
            data["player"][i] = profile
            break
    else:
        data["player"].append(profile)

    print(profile)
    with open(entity_path, "w") as write_file:
        json.dump(data, write_file, indent=4)


def load_player(id):
    """

    :param id:
    :return:
    """
    with open(entity_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for player in data["player"]:
        for stat in player["stats"]:
            value = int(player["stats"][stat])
            player["stats"][stat] = value_to_stat(value, stat)

        for spell in player["spells"]:
            player["spells"][spell] = get_spell_id(player["spells"][spell])

        for item in player["items"]:
            player["items"][item] = get_item_id(player["items"][item])

        player_object = Player(**player)
        players[player["info"]["id"]] = player_object

    return players[id]


def load_enemies():
    """ """
    with open(entity_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for enemy in data["enemy"]:
        for stat in enemy["stats"]:
            value = int(enemy["stats"][stat])
            enemy["stats"][stat] = value_to_stat(value, stat)

        enemies[enemy["info"]["id"]] = Enemy(**enemy)

    for boss in data["boss"]:
        for stat in boss["stats"]:
            value = int(boss["stats"][stat])
            boss["stats"][stat] = value_to_stat(value, stat)

        bosses[boss["info"]["id"]] = Enemy(**boss)


def find_enemy(level, boss_encounter):
    """

    :param level:
    :param boss_encounter:
    :return:
    """
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

    if len(matches) == 0:
        matches = enemies

    who_to_fight = random.choice(list(matches))
    encounter = matches[who_to_fight]

    return encounter


def get_last_entity_id() -> int:
    """

    :return:
    """
    i = 0

    for enemy in enemies:
        id = enemies[enemy].info["id"]
        if id > i:
            i = id

    for boss in bosses:
        id = bosses[boss].info["id"]
        if id > i:
            i = id

    for player in players:
        id = players[player].info["id"]
        if id > i:
            i = id

    return i


def get_enemy_name(name) -> Entity:
    """

    :param name:
    :return:
    """
    for enemy in enemies:
        if name == enemies[enemy].info["name"]:
            return enemy
    return None


def get_enemy_id(i) -> Entity:
    """

    :param i:
    :return:
    """
    for enemy in enemies:
        if i == enemies[enemy].info["id"]:
            return enemy

    return None


# endregion


# TODO: Fix stats added to player
# region Item Manager
def str_to_item(slot, item) -> Item:
    """

    :param slot:
    :param item:
    :return:
    """
    match slot:
        case "helmet":
            return Helmet(**item)
        case "armor":
            return Armor(**item)
        case "boots":
            return Boots(**item)
        case "weapon":
            return Weapon(**item)
        case "accessory":
            return Accessory(**item)
    return None


def load_items():
    """ """

    with open(item_path, "r") as file:
        data = json.load(file)

    for type in data:
        for slot in data[type]:
            item = data[type][slot]

            for stat in item["stats"]:

                value = item["stats"][stat]
                item["stats"][stat] = value_to_stat(value, stat)
                armory[item["info"]["id"]] = str_to_item(slot, item)


def compare_items(item1, item2) -> str:
    """

    :param item1:
    :param item2:
    :return:
    """
    stats1 = item1.stats
    stats2 = item2.stats

    msg = []

    for stat in stats1:
        msg.append([f"{stat.capitalize()}: {stats1[stat].get_value_color()}", f""])
    for i, stat in enumerate(stats2):
        if i < len(stats1):
            msg[i][1] = f"{stat.capitalize()}: {stats2[stat].get_value_color()}"
        else:
            msg.append([f"", f"{stat.capitalize()}: {stats2[stat].get_value_color()}"])

    msg.insert(0, ['Current:", "Dropped:'])
    msg.insert(
        1,
        [
            f"({item1.info['level']}) {item1.info['name']}",
            f"({item2.info['level']}) {item2.info['name']}",
        ],
    )

    msg = tabulate(
        msg,
        headers="firstrow",
    )

    return msg


def get_last_item_id() -> int:
    """

    :return:
    """
    i = 0

    for category in armory:
        for item in armory[category]:
            if item.id > i:
                i = item.id

    return i


def get_item_name(name) -> Item:
    """

    :param name:
    :return:
    """
    for item in armory:
        if name == armory[item].info["name"]:
            return armory[item]
    return None


def get_item_id(i) -> Item:
    """

    :param i:
    :return:
    """
    for id in armory:
        if i == id:
            return armory[i]
    return None


# endregion


# region Spell Manager
def load_spells():
    """ """

    with open(spell_path, "r") as file:
        data = json.load(file)

    for type in ("passive", "direct"):
        for spell in data[type]:
            spell["info"]["name"] = str_to_color(
                f" {spell['info']['name']} ", spell["info"]["color"]
            )

            for stat in spell["stats"]:
                if stat == "effect":
                    for base in spell["stats"]["effect"]:
                        value = int(spell["stats"]["effect"][base])

                        spell["stats"]["effect"][base] = value_to_stat(value, base)
                elif stat == "passive":
                    value = spell["stats"][stat]

                    spell["stats"][stat] = get_spell_id(int(value))
                else:
                    value = spell["stats"][stat]

                    spell["stats"][stat] = value_to_stat(value, stat)

            match type:
                case "direct":
                    spellbook["direct"][spell["info"]["id"]] = Direct(**spell)
                case "passive":
                    spellbook["passive"][spell["info"]["id"]] = Passive(**spell)


def get_last_spell_id() -> int:
    """

    :return:
    """
    i = 0

    for category in spellbook:
        for spell in spellbook[category]:
            if spell.id > i:
                i = spell.id

    return i


def get_spell_name(name) -> Spell:
    """

    :param name:
    :return:
    """
    for category in spellbook:
        for spell in spellbook[category]:
            if spellbook[category][spell].info["name"] == name:
                return spellbook[category][spell]
    return None


def get_spell_id(i) -> Spell:
    """

    :param i:
    :return:
    """
    for category in spellbook:
        for spell in spellbook[category]:
            if spell == i:
                return spellbook[category][spell]
    return None


# endregion
