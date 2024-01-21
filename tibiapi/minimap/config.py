import pathlib
from tibiapi.utils.image import hashit, load


currentPath = pathlib.Path(__file__).parent.resolve()
imagesFolder = f'{currentPath}/images'
buttonsImagesFolder = f'{imagesFolder}/buttons'
floorsLevelsImagesFolder = f'{imagesFolder}/floorsLevels'
floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
images = {
    'buttons': {
        'radarTools': load(f'{buttonsImagesFolder}/radarTools.png'),
    },
    'floorsLevels': {
        0: load(f'{floorsLevelsImagesFolder}/0.png'),
        1: load(f'{floorsLevelsImagesFolder}/1.png'),
        2: load(f'{floorsLevelsImagesFolder}/2.png'),
        3: load(f'{floorsLevelsImagesFolder}/3.png'),
        4: load(f'{floorsLevelsImagesFolder}/4.png'),
        5: load(f'{floorsLevelsImagesFolder}/5.png'),
        6: load(f'{floorsLevelsImagesFolder}/6.png'),
        7: load(f'{floorsLevelsImagesFolder}/7.png'),
        8: load(f'{floorsLevelsImagesFolder}/8.png'),
        9: load(f'{floorsLevelsImagesFolder}/9.png'),
        10: load(f'{floorsLevelsImagesFolder}/10.png'),
        11: load(f'{floorsLevelsImagesFolder}/11.png'),
        12: load(f'{floorsLevelsImagesFolder}/12.png'),
        13: load(f'{floorsLevelsImagesFolder}/13.png'),
        14: load(f'{floorsLevelsImagesFolder}/14.png'),
        15: load(f'{floorsLevelsImagesFolder}/15.png'),
    }
}
floorsLevelsImagesHashes = {}
for floor in floors:
    floorHash = hashit(images['floorsLevels'][floor])
    floorsLevelsImagesHashes[floorHash] = floor
