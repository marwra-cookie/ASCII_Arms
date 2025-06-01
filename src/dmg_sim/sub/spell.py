class Spell:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def get_details(self) -> str:
        """

        :return:
        """
        stats = self.__dict__

        level = stats["info"]["level"]
        name = stats["info"]["name"]

        msg = f"{name} [{level}]".ljust(30)

        for stat in stats["stats"]:
            if stat == "effect":
                for base in stats["stats"]["effect"]:
                    add_stat = stats["stats"]["effect"][base]

                    msg += f"{add_stat.get_value_color()} "
            elif stat == "passive":
                add_stat = stats["stats"][stat]

                msg += f"({add_stat.info["name"]} [{add_stat.info["level"]}] {add_stat.stats["rounds"].value}x)"
            else:
                add_stat = stats["stats"][stat]

                msg += f"{add_stat.get_value_color()} "

        return msg


class Passive(Spell):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Direct(Spell):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
