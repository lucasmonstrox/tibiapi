from numba import njit
import numpy as np
from tibiapi._common.typings import GrayImage
from tibiapi.utils.image import hashit
from .config import numbersImagesHashes


@njit(cache=True, boundscheck=False)
def cleanBackgroundGrayPixels(image: GrayImage) -> GrayImage:
    zeros = np.zeros((8, 22), dtype=np.uint8)
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y, x] == 192:
                zeros[y, x] = 192
    return zeros


def getFullNumberByImage(image: GrayImage, times: int) -> int:
    number = 0
    numbersImagesIndexes = [[132, 154], [104, 126], [76, 98], [48, 70]]
    for i in range(times):
        x0, x1 = numbersImagesIndexes[i]
        numberImage = image[:, x0:x1]
        currentNumber = getNumberByImage(numberImage)
        if i == 0:
            number += currentNumber
            continue
        number += currentNumber * 10 ** (3 * i)
    return number


def getNumberByImage(numberImage: GrayImage) -> int:
    numberImage = cleanBackgroundGrayPixels(numberImage)
    numberImageHAsh = hashit(numberImage)
    return numbersImagesHashes.get(numberImageHAsh, 0)
