import numpy as np
import os
from tibiapi._common.rectImage import RectImage
from tibiapi.battleList import TopBar
from tibiapi.utils.image import load


currentPath = os.path.dirname(os.path.abspath(__file__))


def test_should_match_configure_creatures_button_image():
    battleListImage = load(
        'tests/battleList/images/battleListConfiguringCreatures.png')
    battleListRectImage = RectImage(0, 0, battleListImage)
    topBar = TopBar(battleListRectImage)
    configureCreaturesButton = load(
        'tibiapi/battleList/images/buttons/configureCreaturesPressed.png')
    assert topBar.configureCreaturesButton.x == 133
    assert topBar.configureCreaturesButton.y == 2
    assert topBar.configureCreaturesButton.width == 12
    assert topBar.configureCreaturesButton.height == 12
    np.testing.assert_array_equal(
        topBar.configureCreaturesButton.image, configureCreaturesButton)


def test_should_match_configure_creatures_button_pressed_image():
    battleListImage = load(
        'tests/battleList/images/battleListConfiguringCreatures.png')
    battleListRectImage = RectImage(0, 0, battleListImage)
    topBar = TopBar(battleListRectImage)
    configureCreaturesButton = load(
        'tibiapi/battleList/images/buttons/configureCreaturesPressed.png')
    assert topBar.configureCreaturesButton.x == 133
    assert topBar.configureCreaturesButton.y == 2
    assert topBar.configureCreaturesButton.width == 12
    assert topBar.configureCreaturesButton.height == 12
    np.testing.assert_array_equal(
        topBar.configureCreaturesButton.image, configureCreaturesButton)
