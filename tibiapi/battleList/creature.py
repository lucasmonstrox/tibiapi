class Creature:
    name: str
    healthPercentage: int
    isBeingAttacked: bool

    def __init__(self, name: str, healthPercentage: int = 100, isBeingAttacked: bool = False):
        self.name = name
        self.healthPercentage = healthPercentage
        self.isBeingAttacked = isBeingAttacked
