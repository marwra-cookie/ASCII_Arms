from . import *


class Stat:

    def __init__(self, value, name):
        self.value = value
        self.name = name


class ArmorPenetration(Stat):

    def __init__(self, value):
        name = "Armor Penetration"
        self.icon = "⛓️‍💥"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{dim(red(f"{int(self.value * 100)}"))}% {self.icon}"
        return color


class AttackPower(Stat):

    def __init__(self, value):
        name = "Attack Power"
        self.icon = "⚔️"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{red(self.value)} {self.icon}"
        return color


class CriticalChance(Stat):

    def __init__(self, value):
        name = "Critical Chance"
        self.icon = "🎯"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{bright(red(f"{int(self.value * 100)}"))}% {self.icon}"
        return color


class CriticalDamage(Stat):

    def __init__(self, value):
        name = "Critical Damage"
        self.icon = "💥"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{bright(red(f"{int(self.value * 100)}"))}% {self.icon}"
        return color


class Defense(Stat):

    def __init__(self, value):
        name = "Defense"
        self.icon = "🛡️"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{bright(yellow(self.value))} {self.icon}"
        return color


class Dodge(Stat):

    def __init__(self, value):
        name = "Dodge"
        self.icon = "👟"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{int(self.value * 100)}% {self.icon}"
        return color


class Energy(Stat):

    def __init__(self, value):
        name = "Energy"
        self.icon = "⚡"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{yellow(self.value)} {self.icon}"
        return color


class HealingPower(Stat):

    def __init__(self, value):
        name = "Healing Power"
        self.icon = "️❤️‍🩹"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"️‍{bright(green(self.value))} {self.icon}"
        return color


class Health(Stat):

    def __init__(self, value):
        name = "Health"
        self.icon = "❤️"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{green(self.value)} {self.icon}"
        return color


class Momentum(Stat):

    def __init__(self, value):
        name = "Momentum"
        self.icon = "💨"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{self.value} {self.icon}"
        return color


class Parry(Stat):

    def __init__(self, value):
        name = "Parry"
        self.icon = "🤺"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{int(self.value * 100)}% {self.icon}"
        return color


class Regeneration(Stat):

    def __init__(self, value):
        name = "Regeneration"
        self.icon = "🦇"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{magenta(f"{int(self.value * 100)}")}% {self.icon}"
        return color


class Resistance(Stat):

    def __init__(self, value):
        name = "Resistance"
        self.icon = "🔥"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{bright(cyan(self.value))} {self.icon}"
        return color


class SpellPenetration(Stat):

    def __init__(self, value):
        name = "Spell Penetration"
        self.icon = "💫"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{dim(blue(f"{int(self.value * 100)}"))}% {self.icon}"
        return color


class SpellPower(Stat):

    def __init__(self, value):
        name = "Spell Power"
        self.icon = "☄"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{bright(magenta(self.value))} {self.icon}"
        return color


class AttackBase(Stat):

    def __init__(self, value):
        name = "Base Attack Damage"
        self.icon = "⚔️"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{red(self.value)} {self.icon}"
        return color


class SpellBase(Stat):

    def __init__(self, value):
        name = "Base Spell Damage"
        self.icon = "💫"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{bright(magenta(self.value))} {self.icon}"
        return color


class HealingBase(Stat):

    def __init__(self, value):
        name = "Base Healing"
        self.icon = "❤️‍🩹"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"️{bright(green(self.value))} {self.icon}"
        return color


class Scaling(Stat):
    def __init__(self, value):
        name = "Power Scaling"
        self.icon = "〽️"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = dim(f"{int(self.value * 100)}% {self.icon}")
        return color


class Cost(Stat):
    def __init__(self, value):
        name = "Cost amount"
        self.icon = "⚡"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{red("-")}{yellow(self.value)} {self.icon}"
        return color


class Rounds(Stat):
    def __init__(self, value):
        name = "Number of rounds"
        self.icon = "♻️"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{self.value} {self.icon}"
        return color


class Gain(Stat):
    def __init__(self, value):
        name = "Energy gained"
        self.icon = "⚡"
        super().__init__(value, name)

    def __str__(self) -> str:
        """

        :return:
        """
        return self.name

    def get_value_color(self) -> str:
        """

        :return:
        """
        color = f"{green("+")}{yellow(self.value)} {self.icon}"
        return color
