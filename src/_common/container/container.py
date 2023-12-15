from functools import cached_property
from ..rectImage import makeFromRectImage, RectImage
from .topBar import TopBar


class Container:
    rectImage: RectImage

    def __init__(self, rectImage: RectImage):
        self.rectImage = rectImage

    @cached_property
    def topBar(self) -> TopBar:
        rectImage = makeFromRectImage(self.rectImage, 0, 0, 176, 16)
        return TopBar(rectImage)

    @cached_property
    def isMaximized(self) -> bool:
        """
        Check whether the container is maximized or minimized.

        It will return True when container is maximized or False if it is minimized.
        """
        pixel = self.topBar.maximizeOrMinimizeButton.image[4, 5]
        return pixel[0] != 192 and pixel[1] != 192 and pixel[2] != 192
