from . import *
from .launcher import project_root
import random
import json
import os


players = {}

enemies = {}
bosses = {}

armory = {}

spellbook = {"passive": {}, "direct": {}}

terrain = {}

# region Entity Manager
entity_path = os.path.join(project_root, "database", "entities.json")


def save_player(player):
    """
    Converts a Player object into a JSON-compatible dictionary and updates or appends it
    to the persistent player data file.

    :param player: Player instance to be serialized and saved.
    """
    save = deepcopy(player)
    save_data = {}
    save_data["info"] = save.info
    save_data["stats"] = save.stats
    del save_data["stats"]["base_health"]
    del save_data["stats"]["base_mana"]

    save_data["spells"] = save.spells
    save_data["items"] = save.items
    save_data["kills"] = save.kills

    for stat in save_data["stats"]:
        save_data["stats"][stat] = save_data["stats"][stat].value

    for spell in save_data["spells"]:
        if save_data["spells"][spell] is None:
            save_data["spells"][spell] = None
        else:
            save_data["spells"][spell] = save_data["spells"][spell].info["id"]

    for item in save_data["items"]:
        if save_data["items"][item] is None:
            save_data["items"][item] = None
        else:
            save_data["items"][item] = save_data["items"][item].info["id"]

    for kill in save_data["kills"]:
        save_data["kills"][kill] = save_data["kills"][kill]

    with open(entity_path, "r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    for i, save in enumerate(data["player"]):
        if save["info"]["id"] == save_data["info"]["id"]:
            data["player"][i] = save_data
            break
    else:
        data["player"].append(save_data)

    with open(entity_path, "w") as write_file:
        json.dump(data, write_file, indent=4)


def load_entities():
    """
    Loads enemy and boss data from JSON files and populates the enemies and bosses dicts.
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

        players[player["info"]["id"]] = Player(**player)

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
    Finds an enemy or boss close to the given level.

    :param level: The level of the player.
    :param boss_encounter: Boolean indicating whether to search for a boss.
    :return: A matching enemy or boss entity.
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
    Finds the highest used ID among all entities.

    :return: Maximum integer ID used by any player, enemy, or boss.
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
    Retrieves an enemy by its name.

    :param name: Name string to match.
    :return: Matching enemy entity or None.
    """
    for enemy in enemies:
        if name == enemies[enemy].info["name"]:
            return enemy
    return None


def get_enemy_id(i) -> Entity:
    """
    Retrieves an enemy by its ID.

    :param i: Numeric ID to match.
    :return: Matching enemy entity or None.
    """
    for enemy in enemies:
        if i == enemies[enemy].info["id"]:
            return enemy

    return None


# endregion


# region Item Manager
item_path = os.path.join(project_root, "database", "items.json")


def set_item_quality(name, level) -> str:
    """
    WIP
    """

    match level:
        case 1:
            return dim(name)
        case 2:
            return dim(green(name))
        case 3:
            return dim(blue(name))
        case 4:
            return dim(magenta(name))
        case 5:
            return dim(yellow(name))


def load_items():
    """
    Loads item data from JSON and populates the armory with instantiated items.
    """

    with open(item_path, "r") as file:
        data = json.load(file)

    for type in data:
        for slot in data[type]:
            item = data[type][slot]

            item["info"]["name"] = set_item_quality(
                item["info"]["name"], item["info"]["level"]
            )

            for stat in item["stats"]:
                value = item["stats"][stat]
                item["stats"][stat] = value_to_stat(value, stat)
                armory[item["info"]["id"]] = str_to_item(slot, item)


def compare_items(item_a, item_b) -> str:
    """
    Compares two items and returns a formatted string showing their stats side by side.

    :param item_a: Currently equipped item.
    :param item_b: New item being compared.
    :return: A string table comparing the two items.
    """

    stats_a = item_a.stats
    stats_b = item_b.stats

    msg = []

    for stat in stats_a:
        msg.append([f"{stat.capitalize()}: {stats_a[stat].get_value_color()}", f""])
    for i, stat in enumerate(stats_b):
        if i < len(stats_a):
            msg[i][1] = f"{stat.capitalize()}: {stats_b[stat].get_value_color()}"
        else:
            msg.append([f"", f"{stat.capitalize()}: {stats_b[stat].get_value_color()}"])

    msg.insert(0, ['Current:", "Dropped:'])
    msg.insert(
        1,
        [
            f"({item_a.info['level']}) {item_a.info['name']}",
            f"({item_b.info['level']}) {item_b.info['name']}",
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
    Finds an item in the armory by its name.

    :param name: Name of the item to find.
    :return: Item object or None.
    """
    for item in armory:
        if name == armory[item].info["name"]:
            return armory[item]
    return None


def get_item_id(i) -> Item:
    """
    Retrieves the highest used item ID from the armory.

    :return: Maximum integer item ID.
    """
    for id in armory:
        if i == id:
            return armory[i]
    return None


# endregion


# region Spell Manager
spell_path = os.path.join(project_root, "database", "spells.json")


def load_spells():
    """
    Loads all spells from the database, formats them, and adds them to the global spellbook.
    """

    with open(spell_path, "r") as file:
        data = json.load(file)

    for type in spellbook.keys():
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
    Retrieves the highest spell ID from the spellbook.

    :return: Maximum integer spell ID.
    """
    i = 0

    for category in spellbook:
        for spell in spellbook[category]:
            if spell.id > i:
                i = spell.id

    return i


def get_spell_name(name) -> Spell:
    """
    Finds a spell in the spellbook by its display name.

    :param name: Display name of the spell.
    :return: Spell object or None.
    """
    for category in spellbook:
        for spell in spellbook[category]:
            if spellbook[category][spell].info["name"] == name:
                return spellbook[category][spell]
    return None


def get_spell_id(i) -> Spell:
    """
    Retrieves a spell object by its ID.

    :param i: Integer ID of the spell.
    :return: Spell object or None.
    """
    for category in spellbook:
        for spell in spellbook[category]:
            if spell == i:
                return spellbook[category][spell]
    return None


# endregion


# region Terrain Manager
terrain_path = os.path.join(project_root, "database", "textures.json")


def load_terrain():
    """ """
    with open(terrain_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for sort in data["terrain"]:
        terrain[sort] = data["terrain"][sort]


# endregion
