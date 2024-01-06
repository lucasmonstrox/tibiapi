import numpy as np
from typing import Optional
from src._common.typings import Image
from src.battleList.typings import CreatureList as BattleListCreatures
from .creature import Creature
from .config import creaturesNamesHashes
from .typings import CreatureList
from .utils import getCreatures, getCreaturesBars


class GameWindow:
    closestCreature: Optional[Creature]
    targetCreature: Optional[Creature]

    def getCreatures(self, battleListCreatures: BattleListCreatures, gameWindowImage: Image) -> CreatureList:
        creaturesBars = getCreaturesBars(gameWindowImage)
        return getCreatures(battleListCreatures, creaturesBars, gameWindowImage, creaturesNamesHashes)
