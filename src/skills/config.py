import numpy as np
import pathlib
from src.utils.image import hashit, load


currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
iconsImagesPath = f'{imagesPath}/icons'
digitsImagesPath = f'{imagesPath}/digits'
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
