from numba import njit
import numpy as np


@njit(cache=True, fastmath=True)
def getCreaturesNamesImages(content: np.ndarray, filledSlotsCount: int) -> np.ndarray:
    creaturesNamesImages = np.ascontiguousarray(
        np.zeros((filledSlotsCount, 115), dtype=np.uint8))
    for i in range(filledSlotsCount):
        y = 11 + (i * 22)
        for j, value in enumerate(content[y, 23:138]):
            if value == 192 or value == 247:
                creaturesNamesImages[i, j] = 192
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
