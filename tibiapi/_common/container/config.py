import pathlib
from tibiapi.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()
imagesFolder = f'{currentPath}/images'
buttonsImagesFolder = f'{imagesFolder}/buttons'
images = {
    'buttons': {
        'close': load(f'{buttonsImagesFolder}/close.png'),
        'maximize': load(f'{buttonsImagesFolder}/maximize.png'),
        'minimize': load(f'{buttonsImagesFolder}/minimize.png'),
    },
}
