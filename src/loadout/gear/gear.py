from src.gear_manager import *


class Gear:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        stats = self.__dict__
        msg = f"({stats["level"]})\t{stats["name"]}"

        return msg

    def print_stats(self) -> str:
        stats = self.__dict__

        msg = f"{stats["name"]} - lvl.{stats["level"]}"
        stats.pop("name")
        stats.pop("level")
        sorted(stats)

        for stat in stats:
            if type(stats[stat]) is float:
                msg += f"\n{green("+" + str(int(stats[stat] * 100)) + "%")}"
            else:
                msg += f"\n{green("+" + str(stats[stat]))}"

            msg += print_stat(stat)

        return msg
