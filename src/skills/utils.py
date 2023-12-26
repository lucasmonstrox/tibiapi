from numba import njit
import numpy as np
from src.utils.image import hashit
from .config import numbersImagesHashes


@njit(cache=True)
def cleanBackgroundGrayPixels(image: np.ndarray) -> np.ndarray:
    zeros = np.zeros((8, 22), dtype=np.uint8)
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y, x] == 192:
                zeros[y, x] = 192
    return zeros


def getNumberByImage(numberImage: np.ndarray) -> int:
    numberImage = cleanBackgroundGrayPixels(numberImage)
    numberImageHAsh = hashit(numberImage)
    return numbersImagesHashes.get(numberImageHAsh, 0)
