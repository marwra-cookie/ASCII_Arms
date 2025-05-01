from . import *


class Stats:

    def __init__(self, value, name):
        self.value = value
        self.name = name


class ArmorPenetration(Stats):

    def __init__(self, value):
        name = "Armor Penetration"
        self.icon = "⛓️‍💥"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"️‍{red(self.value)} {self.icon}"
        return color


class AttackPower(Stats):

    def __init__(self, value):
        name = "Attack Power"
        self.icon = "⚔️"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{red(self.value)} {self.icon}"
        return color


class CriticalChance(Stats):

    def __init__(self, value):
        name = "Critical Chance"
        self.icon = "🎯"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{bright(red(f"{int(self.value * 100)}"))}% {self.icon}"
        return color


class CriticalDamage(Stats):

    def __init__(self, value):
        name = "Critical Damage"
        self.icon = "💥"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{bright(red(f"{int(self.value * 100)}"))}% {self.icon}"
        return color


class Defense(Stats):

    def __init__(self, value):
        name = "Defense"
        self.icon = "🛡️"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{bright(yellow(self.value))} {self.icon}"
        return color


class Dodge(Stats):

    def __init__(self, value):
        name = "Dodge"
        self.icon = "👟"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{int(self.value * 100)}% {self.icon}"
        return color


class Energy(Stats):

    def __init__(self, value):
        name = "Energy"
        self.icon = "⚡"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{yellow(self.value)} {self.icon}"
        return color


class HealingPower(Stats):

    def __init__(self, value):
        name = "Healing Power"
        self.icon = "️❤️‍🩹"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"️‍{bright(green(self.value))} {self.icon}"
        return color


class Health(Stats):

    def __init__(self, value):
        name = "Health"
        self.icon = "❤️"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{green(self.value)} {self.icon}"
        return color


class Momentum(Stats):

    def __init__(self, value):
        name = "Momentum"
        self.icon = "💨"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{self.value} {self.icon}"
        return color


class Parry(Stats):

    def __init__(self, value):
        name = "Parry"
        self.icon = "🤺"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{int(self.value * 100)}% {self.icon}"
        return color


class Regeneration(Stats):

    def __init__(self, value):
        name = "Regeneration"
        self.icon = "🦇"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{magenta(f"{int(self.value * 100)}")}% {self.icon}"
        return color


class Resistance(Stats):

    def __init__(self, value):
        name = "Resistance"
        self.icon = "🔥"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{bright(cyan(self.value))} {self.icon}"
        return color


class SpellPenetration(Stats):

    def __init__(self, value):
        name = "Spell Penetration"
        self.icon = "💫"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{dim(blue(f"{int(self.value * 100)}"))}% {self.icon}"
        return color


class SpellPower(Stats):

    def __init__(self, value):
        name = "Spell Power"
        self.icon = "☄"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{bright(magenta(self.value))} {self.icon}"
        return color


class AttackBase(Stats):

    def __init__(self, value):
        name = "Base Attack Damage"
        self.icon = "⚔️"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{red(self.value)} {self.icon}"
        return color


class SpellBase(Stats):

    def __init__(self, value):
        name = "Base Spell Damage"
        self.icon = "💫"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{bright(magenta(self.value))} {self.icon}"
        return color


class HealingBase(Stats):

    def __init__(self, value):
        name = "Base Healing"
        self.icon = "❤️‍🩹"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"️{bright(green(self.value))} {self.icon}"
        return color


class Scaling(Stats):
    def __init__(self, value):
        name = "Power Scaling"
        self.icon = "〽️"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = dim(f"{int(self.value * 100)}% {self.icon}")
        return color


class Cost(Stats):
    def __init__(self, value):
        name = "Cost amount"
        self.icon = "⚡"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{red("-")}{yellow(self.value)} {self.icon}"
        return color


class Rounds(Stats):
    def __init__(self, value):
        name = "Number of rounds"
        self.icon = "♻️"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{self.value} {self.icon}"
        return color


class Gain(Stats):
    def __init__(self, value):
        name = "Energy gained"
        self.icon = "⚡"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{green("+")}{yellow(self.value)} {self.icon}"
        return color
