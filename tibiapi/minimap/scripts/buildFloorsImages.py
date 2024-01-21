import cv2
import numpy as np
import pathlib
from tibiapi.minimap.config import floors
from tibiapi.utils.image import save


currentPath = pathlib.Path(__file__).parent.parent.resolve()
imagesFolder = f'{currentPath}/images/floors/paths'
for floor in floors:
    floorWithPrefix = str(floor).zfill(2)
    floorImage = cv2.imread(
        f'{imagesFolder}/floor-{floorWithPrefix}-map.png')[..., ::-1]
    image = np.zeros((2266, 2772, 3), dtype=np.uint8)
    image[109:2048 + 109, 106:2560 + 106, :] = floorImage
    save(image, f'tibiapi/minimap/images/floors/maps/{floor}.png')
