class Gear:
    """
    Helm: attackPower, spellPower, healingPower, criticalChance, criticalDamage, health, defense, resistance, dodge
    Armor: health, defense, resistance, dodge, parry, regeneration
    Boots: dodge, energy, momentum
    Weapon: attackPower, spellPower, healingPower, criticalChance, criticalDamage, parry, regeneration, energy, momentum
    Accessory: *
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        stats = ""

        for stat in self.__dict__:
            stats += f"\n{stat} {self.__dict__[stat]}"

        return stats
