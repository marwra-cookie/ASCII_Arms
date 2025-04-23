from tabulate import tabulate
from src.graphics import *


class Item:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        stats = self.__dict__

        msg = f"({stats['base']['level']})\t{stats['base']['name']}\t\t"

        for stat in stats["stats"]:
            msg += f" {stats["stats"][stat].color}"

        return msg


class Accessory(Item):
    pass


class Armor(Item):
    pass


class Boots(Item):
    pass


class Helm(Item):
    pass


class Potion:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Weapon(Item):
    pass
