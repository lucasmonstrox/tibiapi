import numpy as np
from typing import List, Optional
from .creature import Creature
from .config import creaturesNamesHashes
from .utils import getCreatures, getCreaturesBars


class GameWindow:
    closestCreature: Optional[Creature]
    targetCreature: Optional[Creature]

    def getCreatures(self, battleListCreatures: List[str], gameWindowImage: np.ndarray) -> List[tuple[str, str, tuple[int, int]]]:
        creaturesBars = getCreaturesBars(gameWindowImage)
        return getCreatures(battleListCreatures, creaturesBars, gameWindowImage, creaturesNamesHashes)
