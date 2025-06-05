from . import *


def check_string(msg) -> bool:
    """
    Checks if the input string characters.
    Only allows alphabetic characters and optional spaces or underscores.

    :param name: The input string to check.
    :return: True if the string is valid, False otherwise.
    """
    return msg.isalpha()


def pad(msg, length) -> str:
    """
    Pads a string with spaces to ensure it reaches the specified length.

    :param msg: The input string to pad.
    :param length: The desired total length of the string.
    :return: The padded string.
    """
    return msg.ljust(length)


def str_to_color(msg, color) -> str:
    """
    Returns a string wrapped in ANSI codes based on the requested color.

    :param msg: The string to be colored.
    :param color: Color name or style (e.g., "red", "fill_blue", "bright").
    :return: ANSI-formatted colored string.
    """
    match color:
        case "white":
            return white(msg)
        case "red":
            return red(msg)
        case "green":
            return green(msg)
        case "yellow":
            return yellow(msg)
        case "blue":
            return blue(msg)
        case "magenta":
            return magenta(msg)
        case "cyan":
            return cyan(msg)
        case "fill_cyan":
            return fill_cyan(msg)
        case "fill_red":
            return fill_red(msg)
        case "fill_green":
            return fill_green(msg)
        case "fill_yellow":
            return fill_yellow(msg)
        case "fill_blue":
            return fill_blue(msg)
        case "fill_magenta":
            return fill_magenta(msg)
        case "fill_cyan":
            return fill_cyan(msg)
        case "dim":
            return dim(msg)
        case "bright":
            return bright(msg)
    return None


def str_to_item(slot, item) -> Item:
    """
    Instantiates an item object of the correct subclass based on the slot.

    :param slot: Slot name (e.g., "helmet", "weapon").
    :param item: Dictionary with item attributes.
    :return: Item subclass instance or None.
    """
    match slot:
        case "helmet":
            return Helmet(**item)
        case "armor":
            return Armor(**item)
        case "boots":
            return Boots(**item)
        case "weapon":
            return Weapon(**item)
        case "accessory":
            return Accessory(**item)
    return None


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
        case "health" | "base_health":
            return Health(int(value))
        case "mana" | "base_mana":
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
