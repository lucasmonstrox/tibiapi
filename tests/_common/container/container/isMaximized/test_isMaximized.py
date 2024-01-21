import pathlib
from tibiapi._common.container.container import Container
from tibiapi._common.rectImage import RectImage
from tibiapi.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()
imagesFolder = f'{currentPath}/images'


def test_should_return_False_when_container_is_minimized():
    image = load(f'{imagesFolder}/containerMinimized.png')
    rectImage = RectImage(0, 0, image)
    container = Container(rectImage)
    assert container.isMaximized == False


def test_should_return_True_when_container_is_maximized():
    image = load(f'{imagesFolder}/containerMaximized.png')
    rectImage = RectImage(0, 0, image)
    container = Container(rectImage)
    assert container.isMaximized == True
