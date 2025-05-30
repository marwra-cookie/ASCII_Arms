from tabulate import tabulate


class Item:

    def __init__(self, **kwargs):
        self.stats = kwargs
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        """

        :return:
        """
        stats = self.__dict__

        level = stats["info"]["level"]
        name = stats["info"]["name"]
        msg = f"({level}) {name}\t"

        for stat in stats["stats"]:
            add_stats = stats["stats"][stat]

            msg += f"{add_stats.get_value_color()}  "

        return msg

    def get_tabulate(self) -> str:
        """

        :return:
        """
        stats = self.__dict__

        level = stats["info"]["level"]
        name = stats["info"]["name"]

        msg = [[f"({level})\t{name}"]]

        for stat in stats["stats"]:
            add_stats = stats["stats"][stat]

            msg.append([f"{add_stats.icon} {add_stats.get_value_color()}"])
        string = tabulate([msg])

        return string


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
