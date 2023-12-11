import numpy as np


class RectImage:
    x: int
    y: int
    width: int
    height: int
    image: np.ndarray

    def __init__(self, x: int, y: int, image):
        self.x = x
        self.y = y
        self.width = len(image[0])
        self.height = len(image)
        self.image = image
