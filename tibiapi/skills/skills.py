from typing import Callable, Optional
from tibiapi._common.container import Container
from tibiapi._common.rectImage import RectImage
from tibiapi.utils.color import isPixelColor
from .config import pixelsIndexesValues
from .typings import BarPercentage
from .utils import cleanColouredPixels, getCapacityLabelPosition, getFullNumberByImage, getHitPointsLabelPosition, getLevelLabelPosition, getLevelPercentage, getManaLabelPosition, getNumberByImage, getSoulPointsLabelPosition, getSpeedLabelPosition, getXpGainRateLabelPosition


class Skills:
    def __init__(self, rectImage: RectImage):
        self.container = Container(rectImage)

    def getCapacity(self) -> Optional[int]:
        return self.getNumberByTimes(getCapacityLabelPosition, 2)

    def getHitPoints(self) -> Optional[int]:
        return self.getNumberByTimes(getHitPointsLabelPosition, 2)

    def getLevel(self) -> Optional[int]:
        return self.getNumberByTimes(getLevelLabelPosition, 2)

    def getLevelPercentage(self) -> Optional[BarPercentage]:
        if not self.levelPercentageBarIsOpen():
            return None
        return getLevelPercentage(self.container.rectImage.image[37:38, 10:154][0, :, 2], pixelsIndexesValues)

    def levelPercentageBarIsOpen(self) -> Optional[bool]:
        if not self.container.isMaximized:
            return None
        return isPixelColor(self.container.rectImage.image[36, 9], (0, 0, 0))

    def getMana(self) -> Optional[int]:
        return self.getNumberByTimes(getManaLabelPosition, 2)

    def getSoulPoints(self) -> Optional[int]:
        return self.getNumberByTimes(getSoulPointsLabelPosition, 1)

    def getSpeed(self) -> Optional[int]:
        return self.getNumberByTimes(getSpeedLabelPosition, 2)

    def getXp(self) -> Optional[int]:
        if not self.container.isMaximized:
            return None
        y = 47 if self.levelPercentageBarIsOpen() else 40
        image = self.container.rectImage.image[y:y + 8, :][:, :, 0]
        return getFullNumberByImage(image, 4)

    def getXpGainRatePercentage(self) -> Optional[int]:
        if not self.container.isMaximized:
            return None
        pos = getXpGainRateLabelPosition(self.container.rectImage.image)
        if pos is None:
            return None
        dirtNumberImage = self.container.rectImage.image[pos[1]                                                         :pos[1] + 8, 118:140][:, :, 1]
        numberImage = cleanColouredPixels(dirtNumberImage)
        return getNumberByImage(numberImage)

    def getNumberByTimes(self, cb: Callable, times: int) -> Optional[int]:
        if not self.container.isMaximized:
            return None
        pos = cb(self.container.rectImage.image)
        if pos is None:
            return None
        dirtNumberImage = self.container.rectImage.image[pos[1]:pos[1] + 8, :][:, :, 1]
        return getFullNumberByImage(dirtNumberImage, times)
