from functools import cached_property
from ..rectImage import makeFromRectImage, RectImage
from .topBar import TopBar


class Container:
    rectImage: RectImage

    def __init__(self, rectImage: RectImage, topBarClass=None):
        self.rectImage = rectImage
        self.topBarClass = topBarClass

    @cached_property
    def topBar(self) -> TopBar:
        rectImage = makeFromRectImage(self.rectImage, 0, 0, 176, 16)
        if self.topBarClass is None:
            return TopBar(rectImage)
        return self.topBarClass(rectImage)

    @cached_property
    def isMaximized(self) -> bool:
        pixel = self.topBar.maximizeOrMinimizeButton.image[4, 5]
        return pixel[0] != 192 and pixel[1] != 192 and pixel[2] != 192
