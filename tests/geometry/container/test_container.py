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


def test_should_assert_close_button_rect_image():
    image = load(f'{currentPath}/battleList.png')
    rectImage = RectImage(0, 0, image)
    container = Container(rectImage)
    closeButtonRectImage = container.getCloseButtonRectImage()
    assert closeButtonRectImage.x == 161
    assert closeButtonRectImage.y == 2
    assert closeButtonRectImage.width == 12
    assert closeButtonRectImage.height == 12


def test_should_assert_maximize_or_minimize_button_rect_image():
    image = load(f'{currentPath}/battleList.png')
    rectImage = RectImage(0, 0, image)
    container = Container(rectImage)
    closeButtonRectImage = container.getMaximizeOrMinimizeButtonRectImage()
    assert closeButtonRectImage.x == 149
    assert closeButtonRectImage.y == 2
    assert closeButtonRectImage.width == 12
    assert closeButtonRectImage.height == 12
