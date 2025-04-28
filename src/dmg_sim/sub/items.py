from tabulate import tabulate


class Items:

    def __init__(self, **kwargs):
        self.stats = kwargs
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        stats = self.__dict__

        level = stats["info"]["level"]
        name = stats["info"]["name"]
        msg = f"({level}) {name}\t"

        for stat in stats["stats"]:
            add_stats = stats["stats"][stat]

            msg += f"{add_stats.get_color()}  "

        return msg

    def get_tabulate(self):
        stats = self.__dict__

        level = stats["info"]["level"]
        name = stats["info"]["name"]

        msg = [[f"({level})\t{name}"]]

        for stat in stats["stats"]:
            add_stats = stats["stats"][stat]

            msg.append([f"{add_stats.icon} {add_stats.get_color()}"])
        string = tabulate([msg])

        return string


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
