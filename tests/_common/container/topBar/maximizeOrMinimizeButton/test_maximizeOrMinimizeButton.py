import numpy as np
import pathlib
from tibiapi._common.container.topBar import TopBar
from tibiapi._common.rectImage import RectImage
from tibiapi.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()
imagesFolder = f'{currentPath}/images'


def test_should_assert_minimize_button():
    image = load(f'{imagesFolder}/topBarMinimized.png')
    rectImage = RectImage(0, 0, image)
    topBar = TopBar(rectImage)
    maximizeButton = load(
        'tibiapi/_common/container/images/buttons/maximize.png')
    assert topBar.maximizeOrMinimizeButton.x == 149
    assert topBar.maximizeOrMinimizeButton.y == 2
    assert topBar.maximizeOrMinimizeButton.width == 12
    assert topBar.maximizeOrMinimizeButton.height == 12
    np.testing.assert_array_equal(
        topBar.maximizeOrMinimizeButton.image, maximizeButton)


def test_should_assert_maximize_button():
    image = load(f'{imagesFolder}/topBar.png')
    rectImage = RectImage(0, 0, image)
    topBar = TopBar(rectImage)
    minimizeButton = load(
        'tibiapi/_common/container/images/buttons/minimize.png')
    assert topBar.maximizeOrMinimizeButton.x == 149
    assert topBar.maximizeOrMinimizeButton.y == 2
    assert topBar.maximizeOrMinimizeButton.width == 12
    assert topBar.maximizeOrMinimizeButton.height == 12
    np.testing.assert_array_equal(
        topBar.maximizeOrMinimizeButton.image, minimizeButton)
