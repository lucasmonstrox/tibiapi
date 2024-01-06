from ..typings import Image
from .rectImage import RectImage


def makeFromRectImage(rectImage: Image, x: int, y: int, width: int, height: int) -> RectImage:
    return RectImage(rectImage.x + x, rectImage.y + y, rectImage.image[y:y + height, x: x + width])
