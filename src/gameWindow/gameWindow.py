from typing import Optional
from .creature import Creature


class GameWindow:
    creatures: list[Creature]
    closestCreature: Optional[Creature]
    targetCreature: Optional[Creature]
