import pathlib
from src.geometry.container import Container
from src.geometry.rectImage import RectImage
from src.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_method_isMaximized_return_True_when_battleList_is_maximized():
    image = load(f'{currentPath}/battleList.png')
    rectImage = RectImage(0, 0, image)
    container = Container(rectImage)
    assert container.isMaximized() == True


def test_should_method_isMaximized_return_False_when_battleList_is_minimized():
    image = load(f'{currentPath}/battleListMinimized.png')
    rectImage = RectImage(0, 0, image)
    container = Container(rectImage)
    assert container.isMaximized() == False
