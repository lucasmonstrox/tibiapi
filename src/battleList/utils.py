from numba import njit
import numpy as np


@njit(cache=True, fastmath=True, boundscheck=False)
def getCreaturesNamesImages(content: np.ndarray, filledSlotsCount: int) -> np.ndarray:
    creaturesNamesImages = np.zeros((filledSlotsCount, 115), dtype=np.uint8)
    for y in range(filledSlotsCount):
        for x, value in enumerate(content[11 + (y * 22), 23:138]):
            if value == 192 or value == 247:
                creaturesNamesImages[y, x] = 192
    return creaturesNamesImages


@njit(cache=True, fastmath=True)
def creaturesCount(innerContent: np.ndarray) -> int:
    creaturesCount = 0
    possibleCreaturesCount = len(innerContent) // 22
    for i in range(possibleCreaturesCount):
        y = (i * 22) + 15
        if innerContent[y, 22] != 0:
            break
        creaturesCount += 1
    return creaturesCount
