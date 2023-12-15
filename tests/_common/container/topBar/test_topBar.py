import numpy as np
import pathlib
from src._common.container.topBar import TopBar
from src._common.rectImage import RectImage
from src.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_assert_minimize_button():
    image = load(f'{currentPath}/topBarMinimized.png')
    rectImage = RectImage(0, 0, image)
    topBar = TopBar(rectImage)
    maximizeButton = load('src/_common/container/images/buttons/maximize.png')
    assert topBar.maximizeOrMinimizeButton.x == 149
    assert topBar.maximizeOrMinimizeButton.y == 2
    assert topBar.maximizeOrMinimizeButton.width == 12
    assert topBar.maximizeOrMinimizeButton.height == 12
    np.testing.assert_array_equal(
        topBar.maximizeOrMinimizeButton.image, maximizeButton)


def test_should_assert_maximize_button():
    image = load(f'{currentPath}/topBar.png')
    rectImage = RectImage(0, 0, image)
    topBar = TopBar(rectImage)
    minimizeButton = load('src/_common/container/images/buttons/minimize.png')
    assert topBar.maximizeOrMinimizeButton.x == 149
    assert topBar.maximizeOrMinimizeButton.y == 2
    assert topBar.maximizeOrMinimizeButton.width == 12
    assert topBar.maximizeOrMinimizeButton.height == 12
    np.testing.assert_array_equal(
        topBar.maximizeOrMinimizeButton.image, minimizeButton)


def test_should_assert_close_button():
    image = load(f'{currentPath}/topBar.png')
    rectImage = RectImage(0, 0, image)
    topBar = TopBar(rectImage)
    closeButton = load('src/_common/container/images/buttons/close.png')
    assert topBar.closeButton.x == 161
    assert topBar.closeButton.y == 2
    assert topBar.closeButton.width == 12
    assert topBar.closeButton.height == 12
    np.testing.assert_array_equal(topBar.closeButton.image, closeButton)
