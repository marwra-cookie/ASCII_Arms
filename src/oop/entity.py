from src.graphics import *
from tabulate import tabulate


class Entity:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        self.spells = [4]

    def get_level(self) -> str:
        return str(self.level)

    def get_attack_power(self) -> str:
        return red(self.attackPower)

    def get_spell_power(self) -> str:
        return bright(magenta(self.spellPower))

    def get_healing_power(self) -> str:
        return bright(green(self.healingPower))

    def get_critical_chance(self) -> str:
        return bright(red(str(int(self.criticalChance * 100)) + "%"))

    def get_critical_damage(self) -> str:
        return bright(red(str(int(self.criticalDamage * 100)) + "%"))

    def get_health(self) -> str:
        return green(self.health)

    def get_defense(self) -> str:
        return bright(yellow(self.defense))

    def get_resistance(self) -> str:
        return bright(cyan(self.resistance))

    def get_dodge(self) -> str:
        return str(int(self.dodge * 100)) + "%"

    def get_parry(self) -> str:
        return str(int(self.parry * 100)) + "%"

    def get_regeneration(self) -> str:
        return str(int(self.regeneration * 100)) + "%"

    def get_momentum(self) -> str:
        return str(self.momentum)

    def get_energy(self) -> str:
        return yellow(self.energy)

    def get_stats(self) -> str:
        str = tabulate(
            [
                [
                    "Health",
                    self.get_health(),
                    "Attack Power",
                    self.get_attack_power(),
                    "Momentum",
                    self.get_momentum(),
                ],
                [
                    "Defense",
                    self.get_defense(),
                    "Spell Power",
                    self.get_spell_power(),
                    "Energy",
                    self.get_energy(),
                ],
                [
                    "Resistance",
                    self.get_resistance(),
                    "Healing Power",
                    self.get_healing_power(),
                ],
                [
                    "Dodge",
                    self.get_dodge(),
                    "Critical Chance",
                    self.get_critical_chance(),
                ],
                [
                    "Parry",
                    self.get_parry(),
                    "Critical Damage",
                    self.get_critical_damage(),
                ],
            ]
        )

        return str

    def get_spells(self) -> str:
        slots = []

        for i, spell in enumerate(self.spells):
            slots.append([f"Spell {i + 1}:", self.spells[i]])

        table = tabulate(slots, headers=["Slot", "Name"])

        return table


class Player(Entity):

    def __init__(self, name):
        stats = {
            "name": name,
            "level": 1,
            "attackPower": 10,
            "spellPower": 10,
            "healingPower": 10,
            "criticalChance": 0.1,
            "criticalDamage": 1.5,
            "armorPenetration": 0,
            "spellPenetration": 0,
            "health": 100,
            "defense": 0,
            "resistance": 0,
            "dodge": 0.05,
            "parry": 0.05,
            "regeneration": 0,
            "energy": 3,
            "momentum": 100,
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


class Enemy(Entity):
    pass
