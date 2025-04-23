class Spells:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        return self.name

    def get_details(self):
        str = f"{self.attackBase}/{self.attackScaling} - {self.spellBase}/{self.spellScaling} - {self.healBase}/{self.healScaling}"

        return str


class Passive(Spells):

    def __init__(self, **kwargs):
        self.rounds = kwargs["rounds"]
        kwargs.pop("rounds")

        super().__init__(**kwargs)

    def get_power(self):
        str = f"{self.attackBase}/{self.attackScaling} - {self.spellBase}/{self.spellScaling} - {self.healBase}/{self.healScaling} ({self.rounds} rounds)"

        return str


class Direct(Spells):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
