import math
from numba import njit, typed, types
import numpy as np
import pathlib
from typing import Dict, List
from src.utils.image import load
from src.wiki.creatures import creatures as wikiCreatures


currentPath = pathlib.Path(__file__).parent.resolve()
creaturesNamesHashes = typed.Dict.empty(
    key_type=types.unicode_type, value_type=types.uint8[:, :, :])
for creature in wikiCreatures:
    creaturesNamesHashes[creature] = load(
        f'{currentPath}/images/monsters/{creature}.png')


@njit(cache=True, boundscheck=False)
def creatureImagesAreSimilar(matrix: np.ndarray, other: np.ndarray) -> bool:
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            pixel = matrix[y, x]
            if other[y, x] == 0 and (pixel != 0 and pixel != 113 and pixel != 29 and pixel != 57 and pixel != 91 and pixel != 152 and pixel != 170 and pixel != 192):
                return False
    return True


@njit(cache=True, boundscheck=False)
def isBlack(pixel: np.ndarray) -> bool:
    return pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0


@njit(cache=True, fastmath=True, boundscheck=False)
def getCreaturesBars(gameWindowImage: np.ndarray) -> List[tuple[int, int]]:
    bars = [(-1, -1)] * 45
    width = len(gameWindowImage[0]) - 27
    height = len(gameWindowImage) - 3
    creatureIndex = 0
    for y in range(height):
        x = -1
        while x < width:
            x += 1
            if isBlack(gameWindowImage[y][x + 26]) == False:
                x += 26
                continue
            if isBlack(gameWindowImage[y][x]) == False:
                continue
            bothBordersAreBlack = True
            for l in range(25):
                if (
                    isBlack(gameWindowImage[y][x + 25 - l]) == False or
                    isBlack(gameWindowImage[y + 3][x + 25 - l]) == False
                ):
                    bothBordersAreBlack = False
                    x += 25 - l
                    break
            if bothBordersAreBlack == False:
                continue
            if (
                isBlack(gameWindowImage[y + 1][x]) == False or
                isBlack(gameWindowImage[y + 2][x]) == False or
                isBlack(gameWindowImage[y + 1][x + 26]) == False or
                isBlack(gameWindowImage[y + 2][x + 26]) == False
            ):
                continue
            bars[creatureIndex] = (x, y)
            creatureIndex += 1
            x += 26
    return np.array([bar for bar in bars if bar[0] != -1])


@njit(cache=True, fastmath=True, boundscheck=False)
def getCreatures(battleListCreatures: List[str], creaturesBars: List[tuple[int, int]], gameWindowImage: np.ndarray, creaturesNamesImages: Dict[int, str]) -> List[tuple[str, str, tuple[int, int]]]:
    numberOfCreaturesBars = len(creaturesBars)
    if numberOfCreaturesBars == 0:
        # using this hack tell numba the correct return type, this will return an empty array
        return [('Unknown', 'unknown', (creatureBar[0], creatureBar[1])) for creatureBar in creaturesBars]
    if numberOfCreaturesBars == 1:
        # TODO: corrigir aqui o monster|unknown
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
    creaturesBars = [creaturesBars[creatureBarIndex]
                     for creatureBarIndex in creaturesBarsSortedIndexes]
    creatureIndex = 0
    alreadyAssertedCreatures = typed.Dict.empty(
        key_type=types.string, value_type=types.bool_)
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
                alreadyAssertedCreatures.get(creatureName, None) is not None
            ):
                continue
            creatureNameImg = creaturesNamesImages.get(creatureName)[:, :, 1]
            creatureNameWidth = len(creatureNameImg[0])
            creatureBarY0 = creatureBar[1] - 13
            creatureBarY1 = creatureBarY0 + 11
            creatureNameImgHalfWidth = math.floor(creatureNameWidth / 2)
            leftDiff = max(creatureNameImgHalfWidth - 13, 0)
            gapLeft = 0 if creatureBar[0] > leftDiff else leftDiff - \
                creatureBar[0]
            gapInnerLeft = 0 if creatureNameWidth > 27 else math.ceil(
                (27 - creatureNameWidth) / 2)
            rightDiff = max(
                creatureNameWidth - creatureNameImgHalfWidth - 14, 0)
            gapRight = 0 if gameWindowWidth > (
                creatureBar[0] + 27 + rightDiff) else creatureBar[0] + 27 + rightDiff - gameWindowWidth
            gapInnerRight = 0 if creatureNameWidth > 27 else math.floor(
                (27 - creatureNameWidth) / 2)
            gg = 13 + gapLeft + gapInnerLeft - gapRight - gapInnerRight
            startingX = max(0, creatureBar[0] - creatureNameImgHalfWidth + gg)
            endingX = min(gameWindowWidth,
                          creatureBar[0] + creatureNameImgHalfWidth + gg)
            creatureWithDirtNameImg = gameWindowImage[creatureBarY0:creatureBarY1,
                                                      startingX:endingX]
            if creatureNameWidth != creatureWithDirtNameImg.shape[1]:
                creatureWithDirtNameImg = gameWindowImage[creatureBarY0:creatureBarY1,
                                                          startingX:endingX + 1]
            if creatureImagesAreSimilar(creatureWithDirtNameImg, creatureNameImg):
                creatures[creatureIndex] = (
                    creatureName, 'monster', (creatureBar[0], creatureBar[1]))
                creatureIndex += 1
                break
            creatureNameImg2 = creaturesNamesImages.get(creatureName)[:, :, 1]
            creatureWithDirtNameImg2 = gameWindowImage[creatureBarY0:creatureBarY1,
                                                       startingX + 1:endingX + 1]
            if creatureNameImg2.shape[1] != creatureWithDirtNameImg2.shape[1]:
                creatureNameImg2 = creatureNameImg2[:,
                                                    0:creatureNameImg2.shape[1] - 1]
            if creatureImagesAreSimilar(creatureWithDirtNameImg2, creatureNameImg2):
                creatures[creatureIndex] = (
                    creatureName, 'monster', (creatureBar[0], creatureBar[1]))
                creatureIndex += 1
                break
            creatureWithDirtNameImg3 = gameWindowImage[creatureBarY0:creatureBarY1,
                                                       startingX:endingX - 1]
            creatureNameImg3 = creaturesNamesImages.get(creatureName)[:, :, 1]
            creatureNameImg3 = creatureNameImg3[:, 1:creatureNameImg3.shape[1]]
            if creatureWithDirtNameImg3.shape[1] != creatureNameImg3.shape[1]:
                creatureNameImg3 = creatureNameImg3[:,
                                                    0:creatureNameImg3.shape[1] - 1]
            if creatureImagesAreSimilar(creatureWithDirtNameImg3, creatureNameImg3):
                creatures[creatureIndex] = (
                    creatureName, 'monster', (creatureBar[0], creatureBar[1]))
                creatureIndex += 1
                break
            assertTryouts += 1
            previousCreatureName = creatureName
            alreadyAssertedCreatures[creatureName] = True
        alreadyAssertedCreatures.clear()
    return creatures
