import numpy as np
import os
from tibiapi.utils.image import hashit, load
from tibiapi.wiki.creatures import creatures


print('__file__', __file__)
print('os.path.abspath(__file__)', os.path.abspath(__file__))
print('os.path.dirname(os.path.abspath(__file__))',
      os.path.dirname(os.path.abspath(__file__)))
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
