from typing import override

from src.loadout.spells.spells import Spells


class Passive(Spells):

    def __init__(self, **kwargs):
        self.rounds = kwargs["rounds"]
        kwargs.pop("rounds")

        super().__init__(**kwargs)

    @override
    def get_power(self):
        str = f"{self.attackBase}/{self.attackScaling} - {self.spellBase}/{self.spellScaling} - {self.healBase}/{self.healScaling} ({self.rounds} rounds)"

        return str