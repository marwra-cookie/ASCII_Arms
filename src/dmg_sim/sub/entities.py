from . import *
from tabulate import tabulate


class Entities:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        self.spells = {
            "Slot 1": None,
            "Slot 2": None,
            "Slot 3": None,
            "Slot 4": None,
        }

    def get_stats(self) -> str:
        stats = self.__dict__

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
            slots.append([f"🔮 {spell}:", self.spells[spell]])

        table = tabulate(slots, headers=["Slot", "Name"])

        return table


class Player(Entities):

    def __init__(self, name):
        self.base = {
            "base_attackPower": 10,
            "base_spellPower": 10,
            "base_healingPower": 10,
            "base_criticalChance": 0.1,
            "base_criticalDamage": 1.5,
            "base_armorPenetration": 0,
            "base_spellPenetration": 0,
            "base_health": 100,
            "base_defense": 0,
            "base_resistance": 0,
            "base_dodge": 0.05,
            "base_parry": 0.05,
            "base_regeneration": 0,
            "base_energy": 3,
            "base_momentum": 100,
        }

        self.items = {
            "accessory": None,
            "armor": None,
            "boots": None,
            "helm": None,
            "potion": None,
            "weapon": None,
        }

        stats = {
            "name": name,
            "level": 1,
            "attackPower": AttackPower(self.base["base_attackPower"]),
            "spellPower": SpellPower(self.base["base_spellPower"]),
            "healingPower": HealingPower(self.base["base_healingPower"]),
            "criticalChance": CriticalChance(self.base["base_criticalChance"]),
            "criticalDamage": CriticalDamage(self.base["base_criticalDamage"]),
            "armorPenetration": ArmorPenetration(self.base["base_armorPenetration"]),
            "spellPenetration": SpellPenetration(self.base["base_spellPenetration"]),
            "health": Health(self.base["base_health"]),
            "defense": Defense(self.base["base_defense"]),
            "resistance": Resistance(self.base["base_resistance"]),
            "dodge": Dodge(self.base["base_dodge"]),
            "parry": Parry(self.base["base_parry"]),
            "regeneration": Regeneration(self.base["base_regeneration"]),
            "energy": Energy(self.base["base_energy"]),
            "momentum": Momentum(self.base["base_momentum"]),
        }

        super().__init__(**stats)

    def add_item(self, item):

        for stat in item.stats:
            getattr(self, stat).value += item.stats[stat].value

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
    pass
