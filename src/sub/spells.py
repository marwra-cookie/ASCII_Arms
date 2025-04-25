class Spells:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        stats = self.__dict__

        msg = f"{type(self).__name__}\t[{stats['basic']['level']}] {stats['basic']['name']}\t"

        for stat in stats["stats"]:
            if stat == "base":
                for base in stats["stats"]["base"]:
                    msg += f" {stats["stats"]["base"][base].get_color()}"
            else:
                msg += f" {stats["stats"][stat].get_color()}"

        return msg


class Passive(Spells):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Direct(Spells):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
