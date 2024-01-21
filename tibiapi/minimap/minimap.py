import numpy as np
from typing import Optional
from tibiapi._common.rectImage.rectImage import RectImage
from tibiapi.minimap.utils import getRadarToolsPosition
from tibiapi.utils.image import hashit
from .config import floorsLevelsImagesHashes


class Minimap:
    coordinate: Optional[tuple[int, int, int]]

    def __init__(self, rectImage: RectImage):
        self.rectImage = rectImage

    def getFloorLevel(self) -> Optional[int]:
        radarToolsPosition = getRadarToolsPosition(self.rectImage.image)
        if radarToolsPosition is None:
            return None
        left, top, width, _ = radarToolsPosition
        left = left + width + 8
        top = top - 7
        floorLevelImage = np.ascontiguousarray(
            self.rectImage.image[top:top + 67, left:left + 2])
        floorLevelImageHash = hashit(floorLevelImage)
        return floorsLevelsImagesHashes.get(floorLevelImageHash, None)
