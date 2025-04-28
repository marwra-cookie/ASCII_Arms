from sub import *


import json


enemies = {}


def load_player(id):

    with open(f"database/entities.json", "r", encoding="utf-8") as file:
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

                return Player(**player)
    return None


def load_enemies():

    with open(f"database/entities.json", "r", encoding="utf-8") as file:
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


def get_last_id():
    i = 0

    for enemy in enemies:
        id = enemy.info["id"]
        if id > i:
            i = id

    return i


def get_enemy_name(name):
    for enemy in enemies:
        if name == enemy.info["name"]:
            return enemy
    return None


def get_enemy_id(i):
    for enemy in enemies:
        if i == enemy.info["id"]:
            return enemy

    return None
