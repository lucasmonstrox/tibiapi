import numpy as np
from typing import Optional
from tibiapi._common.rectImage.rectImage import RectImage
from tibiapi._common.typings import BBox, Image
from tibiapi.utils.image import hashit, locate
from .config import floorsLevelsImagesHashes, images
from .typings import Coordinate
from .utils import getCoordinateFromPixel, getPixelFromCoordinate, getRadarToolsPosition


class Minimap:
    previousCoordinate: Optional[Coordinate]
    previousRadarImageHash: int
    rectImage: RectImage

    def __init__(self, rectImage: RectImage):
        self.previousCoordinate = None
        self.previousRadarImageHash = 0
        self.rectImage = rectImage

    def getCoordinate(self) -> Optional[tuple[int, int, int]]:
        radarImage = self.getRadarImage()
        if radarImage is None:
            self.previousCoordinate = None
            self.previousRadarImageHash = 0
            return self.previousCoordinate
        radarImage = np.ascontiguousarray(radarImage)
        radarImageHash = hashit(radarImage)
        if self.previousRadarImageHash == radarImageHash:
            return self.previousCoordinate
        floorLevel = self.getFloorLevel()
        if floorLevel is None:
            self.previousCoordinate = None
            self.previousRadarImageHash = 0
            return self.previousCoordinate
        radarImage[52, 53] = 128
        radarImage[52, 54] = 128
        radarImage[53, 53] = 128
        radarImage[53, 54] = 128
        radarImage[54, 51] = 128
        radarImage[54, 52] = 128
        radarImage[55, 51] = 128
        radarImage[55, 52] = 128
        radarImage[54, 53] = 128
        radarImage[54, 54] = 128
        radarImage[55, 53] = 128
        radarImage[55, 54] = 128
        radarImage[54, 55] = 128
        radarImage[54, 56] = 128
        radarImage[55, 55] = 128
        radarImage[55, 56] = 128
        radarImage[56, 53] = 128
        radarImage[56, 54] = 128
        radarImage[57, 53] = 128
        radarImage[57, 54] = 128
        if self.previousCoordinate is not None:
            (previousCoordinateXPixel, previousCoordinateYPixel) = getPixelFromCoordinate(
                self.previousCoordinate)
            paddingSize = 5
            yStart = previousCoordinateYPixel - (54 + paddingSize)
            yEnd = previousCoordinateYPixel + (54 + 1 + paddingSize)
            xStart = previousCoordinateXPixel - (53 + paddingSize)
            xEnd = previousCoordinateXPixel + (53 + paddingSize)
            areaImageToCompare = images['floors']['maps'][floorLevel][yStart:yEnd, xStart:xEnd]
            areaFoundImage = locate(
                areaImageToCompare, radarImage, confidence=0.9)
            if areaFoundImage:
                currentCoordinateXPixel = previousCoordinateXPixel - \
                    paddingSize + areaFoundImage[0]
                currentCoordinateYPixel = previousCoordinateYPixel - \
                    paddingSize + areaFoundImage[1]
                (currentCoordinateX, currentCoordinateY) = getCoordinateFromPixel(
                    (currentCoordinateXPixel, currentCoordinateYPixel))
                self.previousCoordinate = (
                    currentCoordinateX, currentCoordinateY, floorLevel)
                self.previousRadarImageHash = radarImageHash
                return self.previousCoordinate
        imageCoordinate = locate(
            images['floors']['maps'][floorLevel], radarImage, confidence=0.75)
        if imageCoordinate is None:
            self.previousCoordinate = None
            self.previousRadarImageHash = 0
            return self.previousCoordinate
        xImgCoordinate = imageCoordinate[0] + 53
        yImgCoordinate = imageCoordinate[1] + 54
        xCoordinate, yCoordinate = getCoordinateFromPixel(
            (xImgCoordinate, yImgCoordinate))
        self.previousCoordinate = (xCoordinate, yCoordinate, floorLevel)
        self.previousRadarImageHash = radarImageHash
        return self.previousCoordinate

    def getFloorLevel(self) -> Optional[int]:
        radarToolsPosition = self.getRadarToolsPosition()
        if radarToolsPosition is None:
            return None
        left, top, width, _ = radarToolsPosition
        left = left + width + 8
        top = top - 7
        floorLevelImage = np.ascontiguousarray(
            self.rectImage.image[top:top + 67, left:left + 2])
        floorLevelImageHash = hashit(floorLevelImage)
        return floorsLevelsImagesHashes.get(floorLevelImageHash, None)

    def getRadarImage(self) -> Optional[Image]:
        radarToolsPosition = self.getRadarToolsPosition()
        if radarToolsPosition is None:
            return None
        x0 = radarToolsPosition[0] - 106 - 11
        x1 = x0 + 106
        y0 = radarToolsPosition[1] - 50
        y1 = y0 + 109
        return self.rectImage.image[y0:y1, x0:x1]

    def getRadarToolsPosition(self) -> Optional[BBox]:
        return getRadarToolsPosition(self.rectImage.image)
