from . import *


class Stat:

    def __init__(self, value, name):
        self.value = value
        self.name = name

    def get_value_color(self) -> str:
        """

        :return:
        """
        return f"{self.icon}{self.color}"


class Penetration(Stat):

    def __init__(self, value):
        name = "Penetration"
        self.icon = "⛓️‍💥"
        self.color = dim(red(f"{int(value * 100)}%"))
        super().__init__(value, name)


class AttackPower(Stat):

    def __init__(self, value):
        name = "Attack Power"
        self.icon = "⚔️"
        self.color = red(value)
        super().__init__(value, name)


class CriticalChance(Stat):

    def __init__(self, value):
        name = "Critical Chance"
        self.icon = "🎯"
        self.color = bright(red(f"{int(value * 100)}%"))
        super().__init__(value, name)


class CriticalDamage(Stat):

    def __init__(self, value):
        name = "Critical Damage"
        self.icon = "💥"
        self.color = bright(red(f"{int(value * 100)}%"))
        super().__init__(value, name)


class Defense(Stat):

    def __init__(self, value):
        name = "Defense"
        self.icon = "🛡️"
        self.color = bright(yellow(value))
        super().__init__(value, name)


class Dodge(Stat):

    def __init__(self, value):
        name = "Dodge"
        self.icon = "🏃‍♂️‍➡️"
        self.color = white(f"{int(value * 100)}%")
        super().__init__(value, name)


class Health(Stat):

    def __init__(self, value):
        name = "Health"
        self.icon = "❤️"
        self.color = green(value)
        super().__init__(value, name)


class Mana(Stat):

    def __init__(self, value):
        name = "Mana"
        self.icon = "🔵"
        self.color = blue(value)
        super().__init__(value, name)


class Momentum(Stat):

    def __init__(self, value):
        name = "Momentum"
        self.icon = "⚡"
        self.color = white(value)
        super().__init__(value, name)


class LifeSteal(Stat):

    def __init__(self, value):
        name = "Life Steal"
        self.icon = "🩸"
        self.color = magenta(f"{int(value * 100)}%")
        super().__init__(value, name)


class Resistance(Stat):

    def __init__(self, value):
        name = "Resistance"
        self.icon = "🔥"
        self.color = bright(cyan(value))
        super().__init__(value, name)


class SpellPower(Stat):

    def __init__(self, value):
        name = "Spell Power"
        self.icon = "☄️"
        self.color = bright(magenta(value))
        super().__init__(value, name)


class AttackBase(Stat):

    def __init__(self, value):
        name = "Base Attack Damage"
        self.icon = "⚔️"
        self.color = red(value)
        super().__init__(value, name)


class SpellBase(Stat):

    def __init__(self, value):
        name = "Base Spell Damage"
        self.icon = "☄️"
        self.color = bright(magenta(value))
        super().__init__(value, name)


class Scaling(Stat):
    def __init__(self, value):
        name = "Power Scaling"
        self.icon = "〽️"
        self.color = dim(f"{int(value * 100)}%")
        super().__init__(value, name)


class Cost(Stat):
    def __init__(self, value):
        name = "Cost amount"
        self.icon = "🔵"
        self.color = f" {red("-")}{yellow(value)}"
        super().__init__(value, name)


class Rounds(Stat):
    def __init__(self, value):
        name = "Number of rounds"
        self.icon = "♻️"
        self.color = white(value)
        super().__init__(value, name)


class Gain(Stat):
    def __init__(self, value):
        name = "Energy gained"
        self.icon = "🔵"
        self.color = f" {green("+")}{yellow(value)}"
        super().__init__(value, name)
