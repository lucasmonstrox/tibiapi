from functools import cached_property
from ..rectImage import makeFromRectImage, RectImage


class TopBar:
    rectImage: RectImage

    def __init__(self, rectImage: RectImage):
        self.rectImage = rectImage

    @cached_property
    def closeButton(self) -> RectImage:
        """
        Retrieve the bounding rectangle image of the close button.
        """
        return makeFromRectImage(self.rectImage, 161, 2, 12, 12)

    @cached_property
    def maximizeOrMinimizeButton(self) -> RectImage:
        """
        Retrieve the bounding rectangle image of the maximize or minimize button.
        """
        return makeFromRectImage(self.rectImage, 149, 2, 12, 12)
