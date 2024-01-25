from typing import Optional
from tibiapi._common.container import Container
from tibiapi._common.rectImage import RectImage
from tibiapi.utils.color import isPixelColor
from .config import pixelsIndexesValues
from .typings import BarPercentage
from .utils import cleanColouredPixels, getCapacityLabelPosition, getFullNumberByImage, getHitPointsLabelPosition, getLevelPercentage, getManaLabelPosition, getNumberByImage, getSoulPointsLabelPosition, getXpGainRateLabelPosition


class Skills:
    def __init__(self, rectImage: RectImage):
        self.container = Container(rectImage)

    def getCapacity(self) -> Optional[int]:
        if not self.container.isMaximized:
            return None
        pos = getCapacityLabelPosition(self.container.rectImage.image)
        if pos is None:
            return None
        dirtNumberImage = self.container.rectImage.image[pos[1]
            :pos[1] + 8, :][:, :, 1]
        return getFullNumberByImage(dirtNumberImage, 2)

    def getHitPoints(self) -> Optional[int]:
        if not self.container.isMaximized:
            return None
        pos = getHitPointsLabelPosition(self.container.rectImage.image)
        if pos is None:
            return None
        dirtNumberImage = self.container.rectImage.image[pos[1]
            :pos[1] + 8, :][:, :, 1]
        return getFullNumberByImage(dirtNumberImage, 2)

    def getLevel(self) -> Optional[int]:
        if not self.container.isMaximized:
            return None
        return getFullNumberByImage(self.container.rectImage.image[26:34, :][:, :, 1], 2)

    def getLevelPercentage(self) -> Optional[BarPercentage]:
        if not self.levelPercentageBarIsOpen():
            return None
        return getLevelPercentage(self.container.rectImage.image[37:38, 10:154][0, :, 2], pixelsIndexesValues)

    def levelPercentageBarIsOpen(self) -> Optional[bool]:
        if not self.container.isMaximized:
            return None
        return isPixelColor(self.container.rectImage.image[36, 9], (0, 0, 0))

    def getMana(self) -> Optional[int]:
        if not self.container.isMaximized:
            return None
        pos = getManaLabelPosition(self.container.rectImage.image)
        if pos is None:
            return None
        dirtNumberImage = self.container.rectImage.image[pos[1]:pos[1] + 8, :][:, :, 1]
        return getFullNumberByImage(dirtNumberImage, 2)

    def getSoulPoints(self) -> Optional[int]:
        if not self.container.isMaximized:
            return None
        pos = getSoulPointsLabelPosition(self.container.rectImage.image)
        if pos is None:
            return None
        dirtNumberImage = self.container.rectImage.image[pos[1]
            :pos[1] + 8, :][:, :, 1]
        return getFullNumberByImage(dirtNumberImage, 2)

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
        dirtNumberImage = self.container.rectImage.image[pos[1]
            :pos[1] + 8, 118:140][:, :, 1]
        numberImage = cleanColouredPixels(dirtNumberImage)
        return getNumberByImage(numberImage)
