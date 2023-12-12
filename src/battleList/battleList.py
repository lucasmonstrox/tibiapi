from functools import cached_property
from ..geometry.container import Container
from ..geometry.rectImage import RectImage
from ..geometry.factories.rectImage import makeFromRectImage


class BattleList:
    container: Container

    def __init__(self, rectImage: RectImage):
        self.container = Container(rectImage)

    @cached_property
    def configureCreaturesButton(self) -> RectImage:
        return makeFromRectImage(self.container.rectImage, 133, 2, 12, 12)

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
        pixel = self.configureCreaturesButton.image[0, 0]
        return pixel[0] == 28 and pixel[1] == 28 and pixel[2] == 28
