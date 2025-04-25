from src.sub.graphics import *


class Stats:

    def __init__(self, value, name):
        self.value = value
        self.name = name


class ArmorPenetration(Stats):

    def __init__(self, value):
        name = "Armor Penetration"
        color = dim(red(f"{int(value * 100)}")) + "%"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = red(self.value)
        return color


class AttackPower(Stats):

    def __init__(self, value):
        name = "Attack Power"
        color = red(value)

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = red(self.value)
        return color


class CriticalChance(Stats):

    def __init__(self, value):
        name = "Critical Chance"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = bright(red(f"{int(self.value * 100)}")) + "%"
        return color


class CriticalDamage(Stats):

    def __init__(self, value):
        name = "Critical Damage"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = bright(red(f"{int(self.value * 100)}")) + "%"
        return color


class Defense(Stats):

    def __init__(self, value):
        name = "Defense"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = bright(yellow(self.value))
        return color


class Dodge(Stats):

    def __init__(self, value):
        name = "Dodge"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{int(self.value * 100)}" + "%"
        return color


class Energy(Stats):

    def __init__(self, value):
        name = "Energy"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = yellow(self.value)
        return color


class HealingPower(Stats):

    def __init__(self, value):
        name = "Healing Power"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = bright(green(self.value))
        return color


class Health(Stats):

    def __init__(self, value):
        name = "Health"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = green(self.value)
        return color


class Momentum(Stats):

    def __init__(self, value):
        name = "Momentum"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{self.value}"
        return color


class Parry(Stats):

    def __init__(self, value):
        name = "Parry"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{int(self.value * 100)}" + "%"
        return color


class Regeneration(Stats):

    def __init__(self, value):
        name = "Regeneration"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = magenta(f"{int(self.value * 100)}") + "%"
        return color


class Resistance(Stats):

    def __init__(self, value):
        name = "Resistance"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = bright(cyan(self.value))
        return color


class SpellPenetration(Stats):

    def __init__(self, value):
        name = "Spell Penetration"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = dim(blue(f"{int(self.value * 100)}")) + "%"
        return color


class SpellPower(Stats):

    def __init__(self, value):
        name = "Spell Power"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = bright(magenta(self.value))
        return color


class AttackBase(Stats):

    def __init__(self, value):
        name = "Base Attack Damage"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = red(self.value)
        return color


class SpellBase(Stats):

    def __init__(self, value):
        name = "Base Spell Damage"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = bright(magenta(self.value))
        return color


class HealingBase(Stats):

    def __init__(self, value):
        name = "Base Healing"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = bright(green(self.value))
        return color


class Scaling(Stats):
    def __init__(self, value):
        name = "Power Scaling"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = dim(f"{int(self.value * 100)}%")
        return color


class Cost(Stats):
    def __init__(self, value):
        name = "Cost amount"
        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{red("-")}{yellow(self.value)}"
        return color


class Rounds(Stats):
    def __init__(self, value):
        name = "Number of rounds"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{self.value}x"
        return color


class Gain(Stats):
    def __init__(self, value):
        name = "Energy gained"

        super().__init__(value, name)

    def __str__(self) -> str:
        return self.name

    def get_color(self) -> str:
        color = f"{green("+")}{yellow(self.value)}"
        return color
