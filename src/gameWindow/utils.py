import math
from numba import njit
import numpy as np
from typing import Dict
from src._common.typings import GrayImage, Image, Pixel
from src.battleList.typings import CreatureList as BattleListCreatures
from .typings import CreatureList, CreaturesBars


@njit(cache=True, boundscheck=False)
def creatureImagesAreSimilar(matrix: Image, other: Image) -> bool:
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            pixel = matrix[y, x]
            if other[y, x] == 0 and (pixel != 0 and pixel != 113 and pixel != 29 and pixel != 57 and pixel != 91 and pixel != 152 and pixel != 170 and pixel != 192):
                return False
    return True


@njit(cache=True, boundscheck=False)
def isBlack(pixel: Pixel) -> bool:
    return pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0


@njit(cache=True, fastmath=True, boundscheck=False)
def getCreaturesBars(gameWindowImage: GrayImage) -> CreaturesBars:
    bars = [(-1, -1)] * 45
    width = len(gameWindowImage[0]) - 27
    height = len(gameWindowImage) - 3
    creatureIndex = 0
    for y in range(height):
        x = -1
        while x < width:
            x += 1
            if isBlack(gameWindowImage[y, x + 26]) == False:
                x += 26
                continue
            if isBlack(gameWindowImage[y, x]) == False:
                continue
            bothBordersAreBlack = True
            for l in range(25):
                if (
                    isBlack(gameWindowImage[y, x + 25 - l]) == False or
                    isBlack(gameWindowImage[y + 3, x + 25 - l]) == False
                ):
                    bothBordersAreBlack = False
                    x += 25 - l
                    break
            if bothBordersAreBlack == False:
                continue
            if (
                isBlack(gameWindowImage[y + 1, x]) == False or
                isBlack(gameWindowImage[y + 2, x]) == False or
                isBlack(gameWindowImage[y + 1, x + 26]) == False or
                isBlack(gameWindowImage[y + 2, x + 26]) == False
            ):
                continue
            bars[creatureIndex] = (x, y)
            creatureIndex += 1
            x += 26
    return np.array([bar for bar in bars if bar[0] != -1])


@njit(cache=True, fastmath=True, boundscheck=False)
def getCreatures(battleListCreatures: BattleListCreatures, creaturesBars: CreaturesBars, gameWindowImage: GrayImage, creaturesNamesImages: Dict[int, str]) -> CreatureList:
    numberOfCreaturesBars = len(creaturesBars)
    if numberOfCreaturesBars == 0:
        # using this hack tell numba the correct return type, this will return an empty array
        return [('Unknown', 'unknown', (creatureBar[0], creatureBar[1])) for creatureBar in creaturesBars]
    if numberOfCreaturesBars == 1:
        return [(battleListCreatures[0], 'monster', (creaturesBars[0][0], creaturesBars[0][1]))]
    creaturesCategories = {creature: battleListCreatures.count(
        creature) for creature in set(battleListCreatures)}
    categoriesCount = len(creaturesCategories)
    # if there is only one category of creature, hash names images calculations can be avoided
    if categoriesCount == 1:
        firstCreatureName = battleListCreatures[0]
        return [(firstCreatureName, 'monster', (creatureBar[0], creatureBar[1])) for creatureBar in creaturesBars]
    creatures = [('Unknown', 'unknown', (-1, -1))] * numberOfCreaturesBars
    gameWindowImage = gameWindowImage[:, :, 1]
    gameWindowWidth = len(gameWindowImage[1])
    gameWindowHeight = len(gameWindowImage[0])
    x = (gameWindowWidth / 2) - 1
    y = (gameWindowHeight / 2) - 1
    sqrt = np.array([
        math.sqrt(((creatureBar[0] - x) ** 2) + ((creatureBar[1] - y) ** 2)) for creatureBar in creaturesBars], dtype=np.float64)
    creaturesBarsSortedIndexes = np.argsort(sqrt, kind='mergesort')
    creaturesBars = [(creaturesBars[creatureBarIndex][0], creaturesBars[creatureBarIndex][1])
                     for creatureBarIndex in creaturesBarsSortedIndexes]
    creatureIndex = 0
    alreadyAssertedCreatures = set()
    for creatureBar in creaturesBars:
        assertTryouts = 0
        previousCreatureName = ''
        for creatureName in battleListCreatures:
            if creatureName == 'Unknown':
                creatures[creatureIndex] = (
                    'Unknown', 'unknown', (creatureBar[0], creatureBar[1]))
                creatureIndex += 1
                break
            if (
                assertTryouts > 0 and
                creatureName != previousCreatureName and
                creatureName in alreadyAssertedCreatures
            ):
                continue
            creatureNameImg = creaturesNamesImages[creatureName][:, :, 1]
            creatureNameWidth = len(creatureNameImg[0])
            creatureBarX = creatureBar[0]
            creatureBarY = creatureBar[1]
            creatureBarY0 = creatureBarY - 13
            creatureBarY1 = creatureBarY0 + 11
            creatureNameImgHalfWidth = math.floor(creatureNameWidth / 2)
            leftDiff = max(creatureNameImgHalfWidth - 13, 0)
            gapLeft = 0 if creatureBarX > leftDiff else leftDiff - \
                creatureBarX
            gapInnerLeft = 0 if creatureNameWidth > 27 else math.ceil(
                (27 - creatureNameWidth) / 2)
            rightDiff = max(
                creatureNameWidth - creatureNameImgHalfWidth - 14, 0)
            gapRight = 0 if gameWindowWidth > (
                creatureBarX + 27 + rightDiff) else creatureBarX + 27 + rightDiff - gameWindowWidth
            gapInnerRight = 0 if creatureNameWidth > 27 else math.floor(
                (27 - creatureNameWidth) / 2)
            gg = 13 + gapLeft + gapInnerLeft - gapRight - gapInnerRight
            startingX = max(0, creatureBarX - creatureNameImgHalfWidth + gg)
            endingX = min(gameWindowWidth,
                          creatureBarX + creatureNameImgHalfWidth + gg)
            creatureWithDirtNameImg = gameWindowImage[creatureBarY0:creatureBarY1,
                                                      startingX:endingX]
            if creatureNameWidth != creatureWithDirtNameImg.shape[1]:
                creatureWithDirtNameImg = gameWindowImage[creatureBarY0:creatureBarY1,
                                                          startingX:endingX + 1]
            if creatureImagesAreSimilar(creatureWithDirtNameImg, creatureNameImg):
                creatures[creatureIndex] = (
                    creatureName, 'monster', (creatureBarX, creatureBarY))
                creatureIndex += 1
                break
            creatureNameImg2 = creaturesNamesImages[creatureName][:, :, 1]
            creatureWithDirtNameImg2 = gameWindowImage[creatureBarY0:creatureBarY1,
                                                       startingX + 1:endingX + 1]
            if creatureNameImg2.shape[1] != creatureWithDirtNameImg2.shape[1]:
                creatureNameImg2 = creatureNameImg2[:,
                                                    0:creatureNameImg2.shape[1] - 1]
            if creatureImagesAreSimilar(creatureWithDirtNameImg2, creatureNameImg2):
                creatures[creatureIndex] = (
                    creatureName, 'monster', (creatureBarX, creatureBarY))
                creatureIndex += 1
                break
            creatureWithDirtNameImg3 = gameWindowImage[creatureBarY0:creatureBarY1,
                                                       startingX:endingX - 1]
            creatureNameImg3 = creaturesNamesImages[creatureName][:, :, 1]
            creatureNameImg3 = creatureNameImg3[:, 1:creatureNameImg3.shape[1]]
            if creatureWithDirtNameImg3.shape[1] != creatureNameImg3.shape[1]:
                creatureNameImg3 = creatureNameImg3[:,
                                                    0:creatureNameImg3.shape[1] - 1]
            if creatureImagesAreSimilar(creatureWithDirtNameImg3, creatureNameImg3):
                creatures[creatureIndex] = (
                    creatureName, 'monster', (creatureBarX, creatureBarY))
                creatureIndex += 1
                break
            assertTryouts += 1
            previousCreatureName = creatureName
            alreadyAssertedCreatures.add(creatureName)
        alreadyAssertedCreatures.clear()
    return creatures
