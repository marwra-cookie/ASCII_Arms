from copy import deepcopy
from . import *
from tabulate import tabulate


class Entity:

    def __init__(self, **kwargs):
        self.base = deepcopy(kwargs)
        self.__dict__.update(kwargs)

    def get_stats(self) -> str:
        """

        :return:
        """
        stats = self.stats

        str = tabulate(
            [
                ["Defensive", "Offensive", "Extra"],
                [
                    f"{stats["health"].name.ljust(10)} {stats["health"].icon}: {stats["health"].color.ljust(5)}",
                    f"{stats["attack_power"].name.ljust(20)} {stats["attack_power"].icon}: {stats["attack_power"].color.ljust(5)}",
                    f"{stats["momentum"].name.ljust(15)} {stats["momentum"].icon}: {stats["momentum"].color.ljust(5)}",
                ],
                [
                    f"{stats["mana"].name.ljust(10)} {stats["mana"].icon}: {stats["mana"].color.ljust(5)}",
                    f"{stats["spell_power"].name.ljust(20)} {stats["spell_power"].icon}: {stats["spell_power"].color.ljust(5)}",
                    f"{stats["penetration"].name.ljust(15)} {stats["penetration"].icon}: {stats["penetration"].color.ljust(5)}",
                ],
                [
                    f"{stats["defense"].name.ljust(10)} {stats["defense"].icon}: {stats["defense"].color.ljust(5)}",
                    f"{stats["critical_chance"].name.ljust(20)} {stats["critical_chance"].icon}: {stats["critical_chance"].color.ljust(5)}",
                    f"{stats["life_steal"].name.ljust(15)} {stats["life_steal"].icon}: {stats["life_steal"].color.ljust(5)}",
                ],
                [
                    f"{stats["resistance"].name.ljust(10)} {stats["resistance"].icon}: {stats["resistance"].color.ljust(5)}",
                    f"{stats["critical_damage"].name.ljust(20)} {stats["critical_damage"].icon}: {stats["critical_damage"].color.ljust(5)}",
                ],
                [
                    f"{stats["dodge"].name.ljust(10)} {stats["dodge"].icon}: {stats["dodge"].color.ljust(5)}",
                ],
            ],
            headers="firstrow",
        )

        return str

    def get_spells(self) -> str:
        """

        :return:
        """
        slots = []
        spells = self.spells
        for i, spell in enumerate(spells):
            if spells[spell] is not None:
                level = spells[spell].info["level"]
                name = spells[spell].info["name"]

                slots.append(
                    [
                        f"Slot {i + 1}:",
                        f"{name.ljust(15)} [{level}]",
                        spells[spell].get_stats(),
                    ]
                )
            else:
                slots.append([f"Slot {i + 1}:", ""])
        table = tabulate(slots, headers=["Slot", "Name", "Stats"])

        return table

    def get_health_bar(self) -> str:
        """

        :return:
        """
        tot_nr = int(self.base["stats"]["health"].value)
        curr_nr = int(self.stats["health"].value)
        curr_percent = curr_nr / tot_nr

        bars = 20
        filled_bars = round(curr_percent * bars)

        health_bar = f"{self.info["name"]} lvl.{self.info["level"]}\n["

        for i in range(bars):
            if i < filled_bars:
                if curr_percent > 0.66:
                    health_bar += green("■")
                elif curr_percent > 0.33:
                    health_bar += yellow("■")
                else:
                    health_bar += red("■")
            else:
                health_bar += " "

        health_bar += f"] {int(curr_percent * 100)}%\n{tot_nr}/{curr_nr}"

        return health_bar

    def attack_given(self, spell):
        """

        :param spell:
        """
        damage = 0
        scaling = spell.stats["scaling"].value

        for effect in spell.stats["effect"]:
            spell_dmg = spell.stats["effect"][effect]["value"].value

            damage += spell_dmg + (self.stats["attack_power"].value * scaling)

        return damage

    def attack_taken(self, damage):
        """

        :param damage:
        """
        mitigated = damage / (1 + self.stats["defense"].value / 100)

        if self.stats["health"].value - mitigated < 0:
            self.stats["health"].value = 0
        else:
            self.stats["health"].value -= mitigated

    def spell_taken(self, damage):
        """

        :param damage:
        """
        mitigated = damage / (1 + self.stats["resistance"].value / 100)

        if self.stats["health"].value - mitigated < 0:
            self.stats["health"].value = 0
        else:
            self.stats["health"].value -= mitigated

    def heal_taken(self, heal):
        """

        :param heal:
        """
        if (self.stats["health"].value + heal) > self.base["stats"]["health"].value:
            self.stats["health"].value = self.base["stats"]["health"].value
        else:
            self.stats["health"].value += heal


class Player(Entity):
    def __init__(self, **stats):
        super().__init__(**stats)
        self.max_level = 20
        self.max_xp = 1000
        self.calc_max_xp()
        self.calc_curr_xp()

        self.boss_requirement = 4

    def get_items(self) -> str:
        """

        :return:
        """

        tab = [["Slot", "Item", "Stats"]]

        if self.items["helmet"]:
            helmet = self.items["helmet"]

            tab.append(
                [
                    f"{"Helmet".ljust(12)}🪖:",
                    f"{helmet.info["name"]} [{helmet.info["level"]}]".ljust(15),
                    helmet.get_stats(),
                ]
            )
        else:
            tab.append([""])

        if self.items["armor"]:
            armor = self.items["armor"]

            tab.append(
                [
                    f"{"Armor".ljust(12)}👕:",
                    f"{armor.info["name"]} [{armor.info["level"]}]".ljust(15),
                    armor.get_stats(),
                ]
            )
        else:
            tab.append([""])

        if self.items["boots"]:
            boots = self.items["boots"]

            tab.append(
                [
                    f"{"Boots".ljust(12)}🥾:",
                    f"{boots.info["name"]} [{boots.info["level"]}]".ljust(15),
                    boots.get_stats(),
                ]
            )
        else:
            tab.append([""])

        if self.items["weapon"]:
            weapon = self.items["weapon"]

            tab.append(
                [
                    f"{"Weapon".ljust(12)}🗡️:",
                    f"{weapon.info["name"]} [{weapon.info["level"]}]".ljust(15),
                    weapon.get_stats(),
                ]
            )
        else:
            tab.append([""])

        if self.items["accessory"]:
            accessory = self.items["accessory"]

            tab.append(
                [
                    f"{"Accessory".ljust(12)}📿:",
                    f"{accessory.info["name"]} [{accessory.info["level"]}]".ljust(15),
                    accessory.get_stats(),
                ]
            )
        else:
            tab.append([""])

        table = tabulate(
            tab,
            headers="firstrow",
        )

        return table

    def add_item(self, item):
        """

        :param item:
        """

        for item_stat in item.stats:
            self.stats[item_stat].value += item.stats[item_stat].value

        self.items[f"{type(item).__name__.lower()}"] = item

    def remove_item(self, item):
        """

        :param item:
        """
        for stat in item.stats:
            getattr(self, stat).value -= item.stats[stat].value

        self.items[f"{type(item).__name__.lower()}"] = None

    def check_requirement(self) -> bool:
        """

        :return:
        """
        if self.kills["slain"] >= self.boss_requirement:
            return True
        return False

    def get_xp_bar(self) -> str:
        """

        :return:
        """
        tot_nr = int(self.max_xp)
        curr_nr = int(self.xp)
        curr_percent = curr_nr / tot_nr if tot_nr > 0 else 0

        bars = 20
        filled_bars = round(curr_percent * bars)
        empty_bars = bars - filled_bars

        xp_bar = "["
        xp_bar += magenta("■") * filled_bars
        xp_bar += "_" * empty_bars
        xp_bar += f"] {curr_nr}/{tot_nr}"

        return xp_bar

    def calc_max_xp(self):
        """

        :return:
        """
        increase = 1.30

        for lvl in range(1, self.info["level"] + 1):
            increase *= 1 + (lvl / 100)
            self.max_xp = int(1000 * increase)

    def calc_curr_xp(self):
        """

        :return:
        """
        if self.info["level"] >= 20:
            self.xp = self.max_xp
        else:
            self.xp = self.info["xp"]

    def add_xp(self, value) -> bool:
        """

        :param value:
        :return:
        """
        self.xp += value

        if self.xp >= self.max_xp:
            level_up = True
            remain = self.xp - self.max_xp
            self.xp = remain

            if self.info["level"] < 20:
                self.info["level"] += 1
                self.calc_max_xp()
            else:
                self.max_xp = "MAX LEVEL"
        else:
            level_up = False
            self.xp += value

        return level_up


class Enemy(Entity):
    def __init__(self, **stats):
        super().__init__(**stats)
