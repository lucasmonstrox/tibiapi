from typing import List, Optional
from .creature import Creature


class GameWindow:
    creatures: List[Creature]
    closestCreature: Optional[Creature]
    targetCreature: Optional[Creature]
