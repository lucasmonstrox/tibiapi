from functools import cached_property
from src.geometry.container import Container
from src.geometry.rectImage import RectImage


class BattleListContainer:
    container: Container

    def __init__(self, rectImage: RectImage):
        self.container = Container(rectImage)

    @cached_property
    def configureCreaturesButton(self) -> RectImage:
        return RectImage.makeFromRectImage(self.container.rectImage, 133, 2, 12, 12)

    @cached_property
    def isConfiguringCreatures(self) -> bool:
        pixel = self.configureCreaturesButton.image[0, 0]
        return pixel[0] == 28 and pixel[1] == 28 and pixel[2] == 28
