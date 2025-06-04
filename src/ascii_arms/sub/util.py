from . import *


def str_to_length(msg, length) -> str:
    """
    Pads a string with spaces to ensure it reaches the specified length.

    :param msg: The input string to pad.
    :param length: The desired total length of the string.
    :return: The padded string.
    """
    return msg.ljust(length)


def value_to_stat(value, stat) -> Stat:
    """
    Converts a numerical value and stat name into a corresponding Stat object.

    :param value: Raw value to be assigned to the stat.
    :param stat: Name of the stat type (e.g., "health", "attack_power").
    :return: An instance of the appropriate Stat subclass, or None if unmatched.
    """
    match stat:
        case "attack_power":
            return AttackPower(int(value))
        case "spell_power":
            return SpellPower(int(value))
        case "critical_chance":
            return CriticalChance(float(value))
        case "critical_damage":
            return CriticalDamage(float(value))
        case "penetration":
            return Penetration(float(value))
        case "momentum":
            return Momentum(int(value))
        case "health":
            return Health(int(value))
        case "mana":
            return Mana(int(value))
        case "defense":
            return Defense(int(value))
        case "resistance":
            return Resistance(int(value))
        case "dodge":
            return Dodge(float(value))
        case "life_steal":
            return LifeSteal(float(value))
        case "attack":
            return AttackBase(int(value))
        case "spell":
            return SpellBase(int(value))
        case "scaling":
            return Scaling(float(value))
        case "cost":
            return Cost(int(value))
        case "gain":
            return Gain(int(value))
        case "rounds":
            return Rounds(int(value))
    return None
