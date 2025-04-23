class Items:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        stats = self.__dict__

        msg = f"({stats['base']['level']})\t{stats['base']['name']}\t\t"

        for stat in stats["stats"]:
            msg += f" {stats["stats"][stat].color}"

        return msg


class Accessory(Items):
    pass


class Armor(Items):
    pass


class Boots(Items):
    pass


class Helm(Items):
    pass


class Potion:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Weapon(Items):
    pass
