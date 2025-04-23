from oop import *
from tabulate import tabulate


class Entities:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        self.spells = [4]

    def get_stats(self) -> str:
        str = tabulate(
            [
                ["Defensive", "", "Offensive", "", "Extra", ""],
                [
                    "Health",
                    self.health.color,
                    "Attack Power",
                    self.attackPower.color,
                    "Momentum",
                    self.momentum.color,
                ],
                [
                    "Defense",
                    self.defense.color,
                    "Spell Power",
                    self.spellPower.color,
                    "Energy",
                    self.energy.color,
                ],
                [
                    "Resistance",
                    self.resistance.color,
                    "Healing Power",
                    self.healingPower.color,
                ],
                [
                    "Dodge",
                    self.dodge.color,
                    "Critical Chance",
                    self.criticalChance.color,
                ],
                [
                    "Parry",
                    self.parry.color,
                    "Critical Damage",
                    self.criticalDamage.color,
                ],
                [
                    "",
                    "",
                    "Armor Penetration",
                    self.armorPenetration.color,
                ],
                [
                    "",
                    "",
                    "Spell Penetration",
                    self.spellPenetration.color,
                ],
            ],
            headers="firstrow",
        )

        return str

    def get_spells(self) -> str:
        slots = []

        for i, spell in enumerate(self.spells):
            slots.append([f"Spell {i + 1}:", self.spells[i]])

        table = tabulate(slots, headers=["Slot", "Name"])

        return table


class Player(Entities):

    def __init__(self, name):
        stats = {
            "name": name,
            "level": 1,
            "attackPower": AttackPower(10),
            "spellPower": SpellPower(10),
            "healingPower": HealingPower(10),
            "criticalChance": CriticalChance(0.1),
            "criticalDamage": CriticalDamage(1.5),
            "armorPenetration": ArmorPenetration(0),
            "spellPenetration": SpellPenetration(0),
            "health": Health(100),
            "defense": Defense(0),
            "resistance": Resistance(0),
            "dodge": Dodge(0.05),
            "parry": Parry(0.05),
            "regeneration": Regeneration(0),
            "energy": Energy(3),
            "momentum": Momentum(100),
        }

        super().__init__(**stats)

        self.gear = {
            "accessory": None,
            "armor": None,
            "boots": None,
            "helm": None,
            "potion": None,
            "weapon": None,
        }

    def get_gear(self) -> str:
        table = tabulate(
            [
                ["Slot", "Item"],
                ["Helm:", self.gear["helm"]],
                ["Armor:", self.gear["armor"]],
                ["Boots:", self.gear["boots"]],
                ["Accessory:", self.gear["accessory"]],
                ["Weapon:", self.gear["weapon"]],
                ["Potion:", self.gear["potion"]],
            ],
            headers="firstrow",
        )

        return table


class Enemy(Entities):
    pass
