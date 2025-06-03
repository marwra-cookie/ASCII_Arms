from tabulate import tabulate


class Item:

    def __init__(self, **kwargs):
        self.stats = kwargs
        self.__dict__.update(kwargs)

    def get_stats(self) -> str:
        """

        :return:
        """
        stats = self.__dict__

        msg = ""

        for stat in stats["stats"]:
            add_stats = stats["stats"][stat]

            msg += f"{add_stats.get_value_color()}  "

        return msg


class Helmet(Item):
    pass


class Armor(Item):
    pass


class Boots(Item):
    pass


class Weapon(Item):
    pass


class Accessory(Item):
    pass
