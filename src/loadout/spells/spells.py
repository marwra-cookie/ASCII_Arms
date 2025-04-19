from tabulate import tabulate

class Spells:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        return self.name

    def get_details(self):
        str = f"{self.attackBase}/{self.attackScaling} - {self.spellBase}/{self.spellScaling} - {self.healBase}/{self.healScaling}"

        return str