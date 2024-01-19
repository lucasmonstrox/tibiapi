import numpy as np
import os
from tibiapi.utils.image import hashit, load
from tibiapi.wiki.creatures import creatures


parentPath = os.path.dirname(os.path.abspath(__file__))
imagesPath = f'{parentPath}/images'
monstersPath = f'{imagesPath}/monsters'
creaturesNamesImagesHashes = {}

for creatureName in creatures:
    creatureNameImage = load(
        f'{monstersPath}/{creatureName}.png')
    creatureNameImage = np.ravel(creatureNameImage[8:9, 0:115][:, :, 0])
    creatureNameImageHash = hashit(creatureNameImage)
    creaturesNamesImagesHashes[creatureNameImageHash] = creatureName
