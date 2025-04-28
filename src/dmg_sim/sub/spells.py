class Spells:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        self.info["description"] += self.create_description()

    def __str__(self) -> str:
        stats = self.__dict__

        class_type = type(self).__name__
        level = stats["info"]["level"]
        name = stats["info"]["name"]

        msg = f"[{level}] {name}\t/{class_type.lower()}\t\t"

        for stat in stats["stats"]:
            if stat == "effect":
                for base in stats["stats"]["effect"]:
                    stat_class = stats["stats"]["effect"][base]["value"]

                    msg += f"{stat_class.get_color()}  "
            else:
                stat_class = stats["stats"][stat]

                msg += f"{stat_class.get_color()}  "

        return msg

    def create_description(self) -> str:
        effects = self.stats["effect"]
        scaling = self.stats["scaling"]
        msg = ""

        first_run = 0
        length = len(effects)

        for base in effects:
            match base:
                case "attack":
                    stat = effects["attack"]["value"]
                    msg += f" dealing {stat.get_color()} (+ {scaling.get_color()}) physical damage"
                    first_run += 1
                case "spell":
                    stat = effects["spell"]["value"]

                    if first_run == 0:
                        msg += f" dealing {stat.get_color()} (+ {scaling.get_color()}) spell damage"
                        first_run += 1
                    elif first_run < length:
                        msg += f", {stat.get_color()} (+ {scaling.get_color()}) spell damage"
                    else:
                        msg += f" and {stat.get_color()} (+ {scaling.get_color()}) spell damage"

                case "healing":
                    stat = effects["healing"]["value"]

                    if first_run == 0:
                        msg += f" healing the caster for {stat.get_color()} (+ {scaling.get_color()})"
                    else:
                        msg += f" and heals the caster for {stat.get_color()} (+ {scaling.get_color()})"

        return msg


class Passive(Spells):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Direct(Spells):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
