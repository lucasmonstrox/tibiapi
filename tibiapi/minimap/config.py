import pathlib
from tibiapi.utils.image import hashit, load


currentPath = pathlib.Path(__file__).parent.resolve()
floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
images = {
    'buttons': {
        'radarTools': load(f'{currentPath}/images/buttons/radarTools.png'),
    },
    'floorsLevels': {
        0: load(f'{currentPath}/images/floorsLevels/0.png'),
        1: load(f'{currentPath}/images/floorsLevels/1.png'),
        2: load(f'{currentPath}/images/floorsLevels/2.png'),
        3: load(f'{currentPath}/images/floorsLevels/3.png'),
        4: load(f'{currentPath}/images/floorsLevels/4.png'),
        5: load(f'{currentPath}/images/floorsLevels/5.png'),
        6: load(f'{currentPath}/images/floorsLevels/6.png'),
        7: load(f'{currentPath}/images/floorsLevels/7.png'),
        8: load(f'{currentPath}/images/floorsLevels/8.png'),
        9: load(f'{currentPath}/images/floorsLevels/9.png'),
        10: load(f'{currentPath}/images/floorsLevels/10.png'),
        11: load(f'{currentPath}/images/floorsLevels/11.png'),
        12: load(f'{currentPath}/images/floorsLevels/12.png'),
        13: load(f'{currentPath}/images/floorsLevels/13.png'),
        14: load(f'{currentPath}/images/floorsLevels/14.png'),
        15: load(f'{currentPath}/images/floorsLevels/15.png'),
    }
}
floorsLevelsImagesHashes = {}
for floor in floors:
    floorHash = hashit(images['floorsLevels'][floor])
    floorsLevelsImagesHashes[floorHash] = floor
