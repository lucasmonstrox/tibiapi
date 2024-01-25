from numba import typed
import numpy as np
import pathlib
from typing import List
from tibiapi.utils.image import hashit, load


currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
iconsImagesPath = f'{imagesPath}/icons'
digitsImagesPath = f'{imagesPath}/digits'
labelsImagesPath = f'{imagesPath}/labels'
images = {
    'digits': {
        0: load(f'{digitsImagesPath}/0.png'),
        1: load(f'{digitsImagesPath}/1.png'),
        2: load(f'{digitsImagesPath}/2.png'),
        3: load(f'{digitsImagesPath}/3.png'),
        4: load(f'{digitsImagesPath}/4.png'),
        5: load(f'{digitsImagesPath}/5.png'),
        6: load(f'{digitsImagesPath}/6.png'),
        7: load(f'{digitsImagesPath}/7.png'),
        8: load(f'{digitsImagesPath}/8.png'),
        9: load(f'{digitsImagesPath}/9.png'),
    },
    'labels': {
        'capacity': load(f'{labelsImagesPath}/capacity.png'),
        'hitPoints': load(f'{labelsImagesPath}/hitPoints.png'),
        'mana': load(f'{labelsImagesPath}/mana.png'),
        'soulPoints': load(f'{labelsImagesPath}/soulPoints.png'),
        'xpGainRate': load(f'{labelsImagesPath}/xpGainRate.png'),
    }
}
numbersImagesHashes = {}
for number in range(1000):
    numberAsString = "{:03d}".format(number)
    digit = int(numberAsString[2])
    digitImage = images['digits'][digit][:, :, 0]
    numberAsImg = np.zeros((8, 22), dtype=np.uint8)
    numberAsImg[:, 22 - 6:22] = digitImage
    hasDecimalDigit = number >= 10
    if hasDecimalDigit:
        decimalDigit = int(numberAsString[1])
        decimalDigitImage = images['digits'][decimalDigit][:, :, 0]
        numberAsImg[:, 22 - 14:22 - 14 + 6] = decimalDigitImage
    hasHundredDigit = number >= 100
    if hasHundredDigit:
        hundredDigit = int(numberAsString[0])
        hundredDigitAsImg = images['digits'][hundredDigit][:, :, 0]
        numberAsImg[:, 0:6] = hundredDigitAsImg
    numberAsImg = np.array(numberAsImg, dtype=np.uint8)
    hashKey = hashit(numberAsImg)
    numbersImagesHashes[hashKey] = number
    if not hasDecimalDigit:
        decimalDigitImage = images['digits'][0][:, :, 0]
        numberAsImg[:, 22 - 14:22 - 14 + 6] = decimalDigitImage
        numberAsImg[:, 0:6] = decimalDigitImage
        numberAsImg = np.array(numberAsImg, dtype=np.uint8)
        hashKey = hashit(numberAsImg)
        numbersImagesHashes[hashKey] = number
    elif not hasHundredDigit:
        decimalDigitImage = images['digits'][0][:, :, 0]
        numberAsImg[:, 0:6] = decimalDigitImage
        numberAsImg = np.array(numberAsImg, dtype=np.uint8)
        hashKey = hashit(numberAsImg)
        numbersImagesHashes[hashKey] = number

pixelsIndexesValues: List[tuple[int, int]] = typed.List([
    (142, 99), (136, 95), (129, 90), (122, 85), (115, 80),
    (108, 75), (101, 70), (93, 65), (86, 60), (79, 55),
    (72, 50), (65, 45), (58, 40), (51, 35), (43, 30),
    (36, 25), (29, 20), (22, 15), (15, 10), (8, 5), (0, 1),
])
