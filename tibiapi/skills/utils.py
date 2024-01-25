from numba import njit
import numpy as np
from typing import List, Optional
from tibiapi._common.typings import BBox, GrayImage, Image
from tibiapi.utils.image import cacheObjectPosition, hashit, locate
from .config import images, numbersImagesHashes


@njit(cache=True, boundscheck=False)
def cleanBackgroundPixels(image: GrayImage) -> GrayImage:
    zeros = np.zeros((8, 22), dtype=np.uint8)
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y, x] == 192:
                zeros[y, x] = 192
    return zeros


@njit(cache=True, boundscheck=False)
def cleanColouredPixels(image: GrayImage) -> GrayImage:
    zeros = np.zeros((8, 22), dtype=np.uint8)
    for y in range(len(image)):
        for x in range(len(image[0])):
            pixel = image[y, x]
            if pixel == 192 or pixel == 173 or pixel == 152:
                zeros[y, x] = 192
    return zeros


@cacheObjectPosition
def getCapacityLabelPosition(image: Image) -> Optional[BBox]:
    return locate(image, images['labels']['capacity'])


def getFullNumberByImage(image: GrayImage, times: int) -> int:
    number = 0
    numbersImagesIndexes = [[132, 154], [104, 126], [76, 98], [48, 70]]
    for i in range(times):
        x0, x1 = numbersImagesIndexes[i]
        numberImage = image[:, x0:x1]
        currentNumber = getNumberByDirtImage(numberImage)
        if i == 0:
            number += currentNumber
            continue
        number += currentNumber * 10 ** (3 * i)
    return number


@cacheObjectPosition
def getHitPointsLabelPosition(image: Image) -> Optional[BBox]:
    return locate(image, images['labels']['hitPoints'])


@njit(cache=True)
def getLevelPercentage(barImage: Image, pixelsIndexesValues: List[tuple[int, int]]) -> int:
    for pixelIndexValue in pixelsIndexesValues:
        if barImage[pixelIndexValue[0]] == 192:
            return pixelIndexValue[1]
    return 0


@cacheObjectPosition
def getManaLabelPosition(image: Image) -> Optional[BBox]:
    return locate(image, images['labels']['mana'])


def getNumberByDirtImage(numberImage: GrayImage) -> int:
    return getNumberByImage(cleanBackgroundPixels(numberImage))


def getNumberByImage(numberImage: GrayImage) -> int:
    numberImageHAsh = hashit(numberImage)
    return numbersImagesHashes.get(numberImageHAsh, 0)


@cacheObjectPosition
def getSoulPointsLabelPosition(image: Image) -> Optional[BBox]:
    return locate(image, images['labels']['soulPoints'])


@cacheObjectPosition
def getSpeedLabelPosition(image: Image) -> Optional[BBox]:
    return locate(image, images['labels']['speed'])


@cacheObjectPosition
def getXpGainRateLabelPosition(image: Image) -> Optional[BBox]:
    return locate(image, images['labels']['xpGainRate'])
