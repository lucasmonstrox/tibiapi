from .creature import Creature


class GameWindow:
    creatures: list[Creature]
    closestCreature: Creature | None
    targetCreature: Creature | None
