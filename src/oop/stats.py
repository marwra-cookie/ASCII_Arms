from src.graphics import *


class Stats:

    def __init__(self, value, name, color):
        self.value = value
        self.name = name
        self.color = color


class ArmorPenetration(Stats):

    def __init__(self, value):
        name = "Armor Penetration"
        color = dim(red(f"{int(value * 100)}")) + "%"

        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class AttackPower(Stats):

    def __init__(self, value):
        name = "Armor Penetration"
        color = red(value)

        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class CriticalChance(Stats):

    def __init__(self, value):
        name = "Critical Chance"
        color = bright(red(f"{int(value * 100)}")) + "%"
        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class CriticalDamage(Stats):

    def __init__(self, value):
        name = "Critical Damage"
        color = bright(red(f"{int(value * 100)}")) + "%"
        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class Defense(Stats):

    def __init__(self, value):
        name = "Defense"
        color = bright(yellow(value))
        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class Dodge(Stats):

    def __init__(self, value):
        name = "Dodge"
        color = f"{int(value * 100)}" + "%"
        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class Energy(Stats):

    def __init__(self, value):
        name = "Energy"
        color = yellow(value)
        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class HealingPower(Stats):

    def __init__(self, value):
        name = "HealingPower"
        color = bright(green(value))
        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class Health(Stats):

    def __init__(self, value):
        name = "Health"
        color = green(value)

        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class Momentum(Stats):

    def __init__(self, value):
        name = "Momentum"
        color = f"{value}"

        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class Parry(Stats):

    def __init__(self, value):
        name = "Parry"
        color = f"{int(value * 100)}" + "%"

        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class Regeneration(Stats):

    def __init__(self, value):
        name = "Regeneration"
        color = magenta(f"{int(value * 100)}") + "%"

        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class Resistance(Stats):

    def __init__(self, value):
        name = "Resistance"
        color = bright(cyan(value))
        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class SpellPenetration(Stats):

    def __init__(self, value):
        name = "Spell Penetration"
        color = dim(blue(f"{int(value * 100)}")) + "%"
        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name


class SpellPower(Stats):

    def __init__(self, value):
        name = "Spell Power"
        color = bright(magenta(value))
        super().__init__(value, name, color)

    def __str__(self) -> str:
        return self.name
