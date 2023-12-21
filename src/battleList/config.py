import numpy as np
import pathlib
from src.utils.image import hashit, load
from src.wiki.creatures import creatures


parentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{parentPath}/images'
monstersPath = f'{imagesPath}/monsters'
creaturesNamesImagesHashes = {}

for creatureName in creatures:
    creatureNameImage = load(
        f'{monstersPath}/{creatureName}.png')
    creatureNameImage = np.ravel(creatureNameImage[8:9, 0:115][:, :, 0])
    creatureNameImageHash = hashit(creatureNameImage)
    creaturesNamesImagesHashes[creatureNameImageHash] = creatureName
