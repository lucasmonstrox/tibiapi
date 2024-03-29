from functools import cached_property
from typing import Optional
from tibiapi._common.container import Container
from tibiapi._common.rectImage import makeFromRectImage, RectImage
from tibiapi._common.typings import Image
from tibiapi.utils.color import isPixelColor
from tibiapi.utils.image import hashit
from .config import creaturesNamesImagesHashes
from .topBar import TopBar
from .typings import CreatureList
from .utils import creaturesCount, getCreaturesNamesImages


class BattleList:
    container: Container

    def __init__(self, rectImage: RectImage):
        self.container = Container(rectImage, topBarClass=TopBar)

    @cached_property
    def innerContent(self) -> Optional[Image]:
        if not self.container.isMaximized:
            return None
        y = 63 if self.isConfiguringCreatures else 15
        return self.container.rectImage.image[y:self.container.rectImage.y - 11, 4:159][:, :, 0]

    @cached_property
    def creatures(self) -> Optional[CreatureList]:
        if not self.container.isMaximized:
            return None
        if self.creaturesCount == 0:
            return []
        creaturesNamesImages = getCreaturesNamesImages(
            self.innerContent, self.creaturesCount)
        return [creaturesNamesImagesHashes.get(
            hashit(creatureNameImage), 'Unknown') for creatureNameImage in creaturesNamesImages]

    @cached_property
    def creaturesCount(self) -> int:
        return creaturesCount(self.innerContent)

    @cached_property
    def togglePlayersButton(self) -> Optional[RectImage]:
        if not self.container.isMaximized:
            return None
        if not self.isConfiguringCreatures:
            return None
        return makeFromRectImage(self.container.rectImage, 23, 17, 20, 20)

    @cached_property
    def hidePlayersButtonIsEnabled(self) -> bool:
        if self.hidePlayersButton is None:
            return False
        pixel = self.hidePlayersButton.image[0, 0]
        return isPixelColor(pixel, (41, 41, 41))

    @cached_property
    def isConfiguringCreatures(self) -> bool:
        pixel = self.container.topBar.configureCreaturesButton.image[0, 0]
        return isPixelColor(pixel, (28, 28, 28))
