import numpy as np
import pathlib
from tibiapi._common.container.topBar import TopBar
from tibiapi._common.rectImage import RectImage
from tibiapi.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()
imagesFolder = f'{currentPath}/images'


def test_should_assert_close_button():
    image = load(f'{imagesFolder}/topBar.png')
    rectImage = RectImage(0, 0, image)
    topBar = TopBar(rectImage)
    closeButton = load('tibiapi/_common/container/images/buttons/close.png')
    assert topBar.closeButton.x == 161
    assert topBar.closeButton.y == 2
    assert topBar.closeButton.width == 12
    assert topBar.closeButton.height == 12
    np.testing.assert_array_equal(topBar.closeButton.image, closeButton)
