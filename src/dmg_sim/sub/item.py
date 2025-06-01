from tabulate import tabulate


class Item:

    def __init__(self, **kwargs):
        self.stats = kwargs
        self.__dict__.update(kwargs)

    def get_details(self) -> str:
        """

        :return:
        """
        stats = self.__dict__

        level = stats["info"]["level"]
        name = stats["info"]["name"]
        msg = f"{name} [{level}]".ljust(20)

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
