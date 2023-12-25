class Creature:
    name: str
    healthPercentage: int
    isAttackingPlayer: bool
    isBeingAttacked: bool
    isUnderRoof: bool
    coordinate: tuple[int, int, int]
    slot: tuple[int, int]
    windowCoordinate: tuple[int, int]
