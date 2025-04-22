from src.entities.entity import Entity
from tabulate import tabulate
from src.gear_manager import *


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

        print(self.gear.get("helm", "None"))
        table = tabulate(
            [
                ["Slot", "Name"],
                ["Helm:", self.gear.get("helm", "None")],
                ["Armor:", self.gear.get("armor", "None")],
                ["Boots:", self.gear.get("boots", "None")],
                ["Accessory:", self.gear.get("accessory", "None")],
                ["Weapon:", self.gear.get("weapon", "None")],
                ["Potion:", self.gear.get("potion", "None")],
            ],
            headers="firstrow",
        )

        return table
