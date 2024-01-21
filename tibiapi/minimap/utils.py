from numba import njit
from typing import Optional
from tibiapi._common.typings import BBox, Image
from tibiapi.utils.image import cacheObjectPosition, locate
from .config import images
from .typings import Coordinate, PixelCoordinate


@njit(cache=True)
def getCoordinateFromPixel(pixelCoordinate: PixelCoordinate) -> Coordinate:
    return pixelCoordinate[0] + (31744 - 106), pixelCoordinate[1] + (30976 - 109)


@njit(cache=True)
def getPixelFromCoordinate(coordinate: Coordinate) -> PixelCoordinate:
    return coordinate[0] - (31744 - 106), coordinate[1] - (30976 - 109)


@cacheObjectPosition
def getRadarToolsPosition(screenshot: Image) -> Optional[BBox]:
    return locate(screenshot, images['buttons']['radarTools'])
