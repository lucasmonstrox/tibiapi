from functools import cached_property
import numpy as np
from .._common.container import Container
from .._common.rectImage import makeFromRectImage, RectImage
from ..utils.image import hashit
from .config import creaturesNamesImagesHashes
from .topBar import TopBar
from .utils import creaturesCount, getCreaturesNamesImages


class BattleList:
    container: Container

    def __init__(self, rectImage: RectImage):
        self.container = Container(rectImage, topBarClass=TopBar)

    @cached_property
    def innerContent(self) -> np.ndarray | None:
        if not self.container.isMaximized:
            return None
        y = 63 if self.isConfiguringCreatures else 15
        return self.container.rectImage.image[y:self.container.rectImage.y - 11, 4:159][:, :, 0]

    @cached_property
    def creatures(self) -> list[str] | None:
        if not self.container.isMaximized:
            return None
        if self.creaturesCount == 0:
            return []
        creaturesNamesImages = getCreaturesNamesImages(
            self.innerContent, self.creaturesCount)
        return [creaturesNamesImagesHashes.get(
            hashit(creatureNameImage), 'Unknonwn') for creatureNameImage in creaturesNamesImages]

    @cached_property
    def creaturesCount(self) -> int:
        return creaturesCount(self.innerContent)

    @cached_property
    def togglePlayersButton(self) -> RectImage | None:
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
        return pixel[0] == 41 and pixel[1] == 41 and pixel[2] == 41

    @cached_property
    def isConfiguringCreatures(self) -> bool:
        pixel = self.container.topBar.configureCreaturesButton.image[0, 0]
        return pixel[0] == 28 and pixel[1] == 28 and pixel[2] == 28
