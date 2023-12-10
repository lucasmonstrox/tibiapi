from .rectImage import RectImage


class Container:
    rectImage: RectImage

    def __init__(self, rectImage: RectImage):
        self.rectImage = rectImage

    def isMaximized(self) -> bool:
        pixel = self.rectImage.image[5, 154]
        return pixel[0] == 192 and pixel[1] == 192 and pixel[2] == 192
