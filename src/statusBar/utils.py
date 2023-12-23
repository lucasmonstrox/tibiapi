from numba import njit
import numpy as np
from src.utils.color import isPixelColor


@njit(cache=True)
def healthPercentage(bar: np.ndarray) -> int:
    if isPixelColor(bar[93], (49, 46, 100)):
        return 100
    pixelColor = (79, 79, 219)
    if isPixelColor(bar[84], pixelColor):
        return 90
    if isPixelColor(bar[74], pixelColor):
        return 80
    if isPixelColor(bar[65], pixelColor):
        return 70
    if isPixelColor(bar[55], pixelColor):
        return 60
    if isPixelColor(bar[46], pixelColor):
        return 50
    if isPixelColor(bar[37], pixelColor):
        return 40
    if isPixelColor(bar[27], pixelColor):
        return 30
    if isPixelColor(bar[18], pixelColor):
        return 20
    if isPixelColor(bar[8], pixelColor):
        return 10
    if isPixelColor(bar[4], pixelColor):
        return 5
    return 0


@njit(cache=True)
def manaPercentage(bar: np.ndarray) -> int:
    if isPixelColor(bar[93], (105, 45, 45)):
        return 100
    pixelColor = (218, 80, 83)
    if isPixelColor(bar[84], pixelColor):
        return 90
    if isPixelColor(bar[74], pixelColor):
        return 80
    if isPixelColor(bar[65], pixelColor):
        return 70
    if isPixelColor(bar[55], pixelColor):
        return 60
    if isPixelColor(bar[46], pixelColor):
        return 50
    if isPixelColor(bar[37], pixelColor):
        return 40
    if isPixelColor(bar[27], pixelColor):
        return 30
    if isPixelColor(bar[18], pixelColor):
        return 20
    if isPixelColor(bar[8], pixelColor):
        return 10
    if isPixelColor(bar[4], pixelColor):
        return 5
    return 0
