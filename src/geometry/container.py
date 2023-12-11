from .rectImage import RectImage


class Container:
    rectImage: RectImage

    def __init__(self, rectImage: RectImage):
        self.rectImage = rectImage

    def getCloseButtonRectImage(self) -> RectImage:
        """
        Retrieve the bounding rectangle image of the close button in a specific container.
        """
        return RectImage.makeFromRectImage(self.rectImage, 161, 2, 12, 12)

    def getMaximizeOrMinimizeButtonRectImage(self) -> RectImage:
        """
        Retrieve the bounding rectangle image of the maximize or minimize button.
        """
        return RectImage.makeFromRectImage(self.rectImage, 149, 2, 12, 12)

    def isMaximized(self) -> bool:
        """
        Check whether the container is maximized or minimized.

        It will return True when container is maximized or False if it is minimized.
        """
        pixel = self.rectImage.image[5, 154]
        return pixel[0] != 192 and pixel[1] != 192 and pixel[2] != 192
