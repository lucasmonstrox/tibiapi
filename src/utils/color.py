from numba import njit


@njit(cache=True)
def isPixelColor(pixel: tuple[int, int, int], color: tuple[int, int, int]) -> bool:
    return pixel[0] == color[0] and pixel[1] == color[1] and pixel[2] == color[2]
