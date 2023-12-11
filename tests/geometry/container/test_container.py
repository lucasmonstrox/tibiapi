import pathlib
from src.geometry.container import Container
from src.geometry.rectImage import RectImage
from src.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_method_isMaximized_return_True_when_battleList_is_maximized():
    image = load(f'{currentPath}/battleList.png')
    rectImage = RectImage(0, 0, image)
    container = Container(rectImage)
    assert container.isMaximized == True


def test_should_method_isMaximized_return_False_when_battleList_is_minimized():
    image = load(f'{currentPath}/battleListMinimized.png')
    rectImage = RectImage(0, 0, image)
    container = Container(rectImage)
    assert container.isMaximized == False


def test_should_assert_close_button_coordinate_and_dimension():
    image = load(f'{currentPath}/battleList.png')
    rectImage = RectImage(0, 0, image)
    container = Container(rectImage)
    assert container.closeButton.x == 161
    assert container.closeButton.y == 2
    assert container.closeButton.width == 12
    assert container.closeButton.height == 12


def test_should_assert_maximize_or_minimize_button_coordinate_and_dimension():
    image = load(f'{currentPath}/battleList.png')
    rectImage = RectImage(0, 0, image)
    container = Container(rectImage)
    assert container.maximizeOrMinimizeButton.x == 149
    assert container.maximizeOrMinimizeButton.y == 2
    assert container.maximizeOrMinimizeButton.width == 12
    assert container.maximizeOrMinimizeButton.height == 12
