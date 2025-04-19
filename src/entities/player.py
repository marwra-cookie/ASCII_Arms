from src.entities.entity import Entity
from tabulate import tabulate
from src.manager import *

class Player(Entity):

    def __init__(self, name):
        super().__init__(name)

        self.lvl = 1
        self.attackPower = 10
        self.spellPower = 10
        self.healingPower = 10
        self.criticalChance = 0.1
        self.criticalDamage = 1.5

        self.health = 100
        self.defense = 0
        self.resistance = 0
        self.dodge = 0.05
        self.parry = 0.05
        self.regeneration = 0

        self.energy = 3
        self.momentum = 100

        self.gear = {
            "accessory": None,
            "armor": None,
            "boots": None,
            "helm": None,
            "potion": None,
            "weapon": None
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
                ["Potion:", self.gear["potion"]]
            ]
        , headers="firstrow")

        return table