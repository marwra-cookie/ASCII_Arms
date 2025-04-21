from src.entities.entity import Entity
from tabulate import tabulate
from src.manager import *


class Player(Entity):

    def __init__(self, name):
        stats = {
            "name": name,
            "lvl": 1,
            "attackPower": 10,
            "spellPower": 10,
            "healingPower": 10,
            "criticalChance": 0.1,
            "criticalDamage": 1.5,
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
                ["Slot", "Name"],
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
