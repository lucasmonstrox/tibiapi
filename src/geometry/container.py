from .rectImage import RectImage


class Container:
    rectImage: RectImage

    def __init__(self, rectImage: RectImage):
        self.rectImage = rectImage

    def getCloseButtonRectImage(self) -> RectImage:
        return RectImage(161, 2, self.rectImage.image[2:14, 161:173])

    def isMaximized(self) -> bool:
        pixel = self.rectImage.image[5, 154]
        return pixel[0] != 192 and pixel[1] != 192 and pixel[2] != 192
