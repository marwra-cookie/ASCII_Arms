import json
import random

from sub import *


spellbook = {"direct": [], "passive": []}


def load_spells():
    """"""

    spell_types = list(spellbook.keys())

    with open(f"database/spells.json", "r") as file:
        data = json.load(file)

        for g in spell_types:
            for spell in data[g]:

                for stat in spell["stats"]:
                    if stat == "base":
                        for base in spell["stats"]["base"]:
                            match base:
                                case "attackBase":
                                    spell["stats"]["base"][base] = AttackBase(
                                        spell["stats"]["base"][base]
                                    )
                                case "spellBase":
                                    spell["stats"]["base"][base] = SpellBase(
                                        spell["stats"]["base"][base]
                                    )
                                case "healingBase":
                                    spell["stats"]["base"][base] = HealingBase(
                                        spell["stats"]["base"][base]
                                    )
                    else:
                        match stat:
                            case "scaling":
                                spell["stats"][stat] = Scaling(spell["stats"][stat])
                            case "cost":
                                spell["stats"][stat] = Cost(spell["stats"][stat])
                            case "rounds":
                                spell["stats"][stat] = Rounds(spell["stats"][stat])
                            case "gain":
                                spell["stats"][stat] = Gain(spell["stats"][stat])
                match g:
                    case "direct":
                        spellbook[g].append(Direct(**spell))
                    case "passive":
                        spellbook[g].append(Passive(**spell))


def get_last_id():
    i = 0

    for category in spellbook:
        for spell in spellbook[category]:
            if spell.id > i:
                i = spell.id

    return i


def get_spell_name(name):
    for category in spellbook:
        for spell in spellbook[category]:
            if spell.basic["name"] == name:
                return spell
    return None


def get_spell_id(i):
    for category in spellbook:
        for spell in spellbook[category]:
            if spell.basic["id"] == i:
                return spell
    return None
