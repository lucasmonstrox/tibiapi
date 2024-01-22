import numpy as np
from typing import Optional
from tibiapi._common.rectImage.rectImage import RectImage
from tibiapi.utils.image import hashit, locate
from .config import floorsLevelsImagesHashes, images
from .typings import Coordinate
from .utils import getCoordinateFromPixel, getPixelFromCoordinate


class Minimap:
    previousCoordinate: Optional[Coordinate]
    previousRadarImageHash: int
    rectImage: RectImage

    def __init__(self, rectImage: RectImage):
        self.previousCoordinate = None
        self.previousRadarImageHash = 0
        self.rectImage = rectImage

    def getCoordinate(self) -> Optional[Coordinate]:
        radarImage = self.rectImage.image[3:112, 9:115]
        radarImage = np.ascontiguousarray(radarImage)
        radarImageHash = hashit(radarImage)
        if self.previousRadarImageHash == radarImageHash:
            return self.previousCoordinate
        floorLevel = self.getFloorLevel()
        if floorLevel is None:
            self.previousCoordinate = None
            self.previousRadarImageHash = 0
            return self.previousCoordinate
        radarImage[52:58, 53:55] = 128
        radarImage[54:56, 51:57] = 128
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

    def getFloorLevel(self) -> int:
        floorLevelImage = np.ascontiguousarray(
            self.rectImage.image[46:113, 154:156])
        floorLevelImageHash = hashit(floorLevelImage)
        return floorsLevelsImagesHashes.get(floorLevelImageHash, None)
