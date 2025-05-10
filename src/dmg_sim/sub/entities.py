from copy import deepcopy

from . import *
from tabulate import tabulate


class Entities:

    def __init__(self, **kwargs):
        self.base = deepcopy(kwargs)
        self.__dict__.update(kwargs)

    def __str__(self):
        return f"{self.info["id"]}:\t{self.info["name"]} {self.info["icon"]}  lvl.{self.info["level"]}"

    def get_stats(self) -> str:
        stats = self.stats

        str = tabulate(
            [
                ["Defensive", "Offensive", "Extra"],
                [
                    f"{stats["health"].name}: {stats["health"].get_color()}",
                    f"{stats["attackPower"].name}: {stats["attackPower"].get_color()}",
                    f"{stats["momentum"].name}: {stats["momentum"].get_color()}",
                ],
                [
                    f"{stats["defense"].name}: {stats["defense"].get_color()}",
                    f"{stats["spellPower"].name}: {stats["spellPower"].get_color()}",
                    f"{stats["energy"].name}: {stats["energy"].get_color()}",
                ],
                [
                    f"{stats["resistance"].name}: {stats["resistance"].get_color()}",
                    f"{stats["healingPower"].name}: {stats["healingPower"].get_color()}",
                ],
                [
                    f"{stats["dodge"].name}: {stats["dodge"].get_color()}",
                    f"{stats["criticalChance"].name}: {stats["criticalChance"].get_color()}",
                ],
                [
                    f"{stats["parry"].name}: {stats["parry"].get_color()}",
                    f"{stats["criticalDamage"].name}: {stats["criticalDamage"].get_color()}",
                ],
                [
                    f"{stats["regeneration"].name}: {stats["regeneration"].get_color()}",
                    f"{stats["armorPenetration"].name}: {stats["armorPenetration"].get_color()}",
                ],
                [
                    "",
                    f"{stats["spellPenetration"].name}: {stats["spellPenetration"].get_color()}",
                ],
            ],
            headers="firstrow",
        )

        return str

    def get_spells(self) -> str:
        slots = []

        for i, spell in enumerate(self.spells):
            slots.append([f"{spell}:", self.spells[spell]])

        table = tabulate(slots, headers=["Slot", "Name"])

        return table

    def attack_given(self, spell):
        damage = 0
        scaling = spell.stats["scaling"].value

        for effect in spell.stats["effect"]:
            spell_dmg = spell.stats["effect"][effect]["value"].value

            damage += spell_dmg + (self.stats["attackPower"].value * scaling)

        return damage

    def attack_taken(self, damage):
        mitigated = damage / (1 + self.stats["defense"].value / 100)

        if self.stats["health"].value - mitigated < 0:
            self.stats["health"].value = 0
        else:
            self.stats["health"].value -= mitigated

    def spell_taken(self, damage):
        mitigated = damage / (1 + self.stats["resistance"].value / 100)

        if self.stats["health"].value - mitigated < 0:
            self.stats["health"].value = 0
        else:
            self.stats["health"].value -= mitigated

    def heal_taken(self, heal):
        if (self.stats["health"].value + heal) > self.base["stats"]["health"].value:
            self.stats["health"].value = self.base["stats"]["health"].value
        else:
            self.stats["health"].value += heal


class Player(Entities):

    def __init__(self, **stats):
        super().__init__(**stats)

        self.slain = 0

    def add_item(self, item):

        for item_stat in item.stats:
            player_stats = self.stats
            print(player_stats)
            self.stats[item_stat].value += item.stats[item_stat].value

        self.items[f"{type(item).__name__.lower()}"] = item

    def remove_item(self, item):

        for stat in item.stats:
            getattr(self, stat).value -= item.stats[stat].value

        self.items[f"{type(item).__name__.lower()}"] = None

    def get_items(self) -> str:
        table = tabulate(
            [
                ["Slot", "Item"],
                ["🪖 Helm:", self.items["helm"]],
                ["👕 Armor:", self.items["armor"]],
                ["🥾 Boots:", self.items["boots"]],
                ["📿 Accessory:", self.items["accessory"]],
                ["🗡️ Weapon:", self.items["weapon"]],
                ["🧪 Potion:", self.items["potion"]],
            ],
            headers="firstrow",
        )

        return table


class Enemy(Entities):

    def __init__(self, **stats):
        super().__init__(**stats)
