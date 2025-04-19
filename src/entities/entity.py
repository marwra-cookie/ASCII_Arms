from colorama import Fore
from tabulate import tabulate

class Entity:

    def __init__(self, name):
        self.name = name
        self.lvl = 1

        self.attackPower = None
        self.spellPower = None
        self.healingPower = None
        self.criticalChance = None
        self.criticalDamage = None

        self.health = None
        self.defense = None
        self.resistance = None
        self.dodge = None
        self.parry = None
        self.regeneration = None

        self.momentum = None
        self.energy = None

        self.spells = [4]

    def get_lvl(self) -> str:
        return f"{self.lvl}"

    def get_attack_power(self) -> str:
        return Fore.RED + f"{self.attackPower}" + Fore.RESET

    def get_spell_power(self) -> str:
        return Fore.LIGHTMAGENTA_EX + f"{self.spellPower}" + Fore.RESET

    def get_healing_power(self) -> str:
        return Fore.LIGHTGREEN_EX + f"{self.healingPower}" + Fore.RESET

    def get_critical_chance(self) -> str:
        return Fore.LIGHTRED_EX + f"{self.criticalChance * 100}%" + Fore.RESET

    def get_critical_damage(self) -> str:
        return Fore.LIGHTRED_EX + f"{self.criticalDamage * 100}%" + Fore.RESET

    def get_health(self) -> str:
        return Fore.GREEN + f"{self.health}" + Fore.RESET

    def get_defense(self) -> str:
        return Fore.LIGHTYELLOW_EX + f"{self.defense}" + Fore.RESET

    def get_resistance(self) -> str:
        return Fore.LIGHTCYAN_EX + f"{self.resistance}" + Fore.RESET

    def get_dodge(self) -> str:
        return f"{self.dodge * 100}%"

    def get_parry(self) -> str:
        return f"{self.parry * 100}%"

    def get_regeneration(self) -> str:
        return f"{self.regeneration * 100}%"

    def get_momentum(self) -> str:
        return f"{self.momentum}"

    def get_energy(self) -> str:
        return Fore.YELLOW + f"{self.energy}" + Fore.RESET

    def get_stats(self) -> str:
        str = tabulate(
            [
                [
                    "Attack Power",
                    self.get_attack_power(),
                    "Health",
                    self.get_health(),
                    "Momentum",
                    self.get_momentum(),
                ],
                [
                    "Spell Power",
                    self.get_spell_power(),
                    "Defense",
                    self.get_defense(),
                    "Energy",
                    self.get_energy(),
                ],
                [
                    "Healing Power",
                    self.get_healing_power(),
                    "Resistance",
                    self.get_resistance(),
                ],
                ["Critical Chance", self.get_critical_chance(), "Dodge", self.get_dodge()],
                ["Critical Damage", self.get_critical_damage(), "Parry", self.get_parry()]
            ])

        return str

    def get_spells(self) -> str:
        slots = []

        for i, spell in enumerate(self.spells):
            slots.append([f"Spell {i + 1}:", self.spells[i]])

        table = tabulate(slots, headers=["Slot", "Name"])

        return table