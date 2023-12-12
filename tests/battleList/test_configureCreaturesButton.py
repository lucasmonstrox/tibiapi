import numpy as np
import pathlib
from src.battleList.battleList import BattleList
from src.geometry.rectImage import RectImage
from src.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_match_configure_creatures_button_image():
    battleListImage = load(f'{currentPath}/images/battleListNotConfiguringCreatures.png')
    battleListRectImage = RectImage(0, 0, battleListImage)
    battleList = BattleList(battleListRectImage)
    configureCreaturesButton = load('src/battleList/images/buttons/configureCreatures.png')
    assert battleList.configureCreaturesButton.x == 133
    assert battleList.configureCreaturesButton.y == 2
    assert battleList.configureCreaturesButton.width == 12
    assert battleList.configureCreaturesButton.height == 12
    np.testing.assert_array_equal(battleList.configureCreaturesButton.image, configureCreaturesButton)

def test_should_match_configure_creatures_button_pressed_image():
    battleListImage = load(f'{currentPath}/images/battleListConfiguringCreatures.png')
    battleListRectImage = RectImage(0, 0, battleListImage)
    battleList = BattleList(battleListRectImage)
    configureCreaturesButton = load('src/battleList/images/buttons/configureCreaturesPressed.png')
    assert battleList.configureCreaturesButton.x == 133
    assert battleList.configureCreaturesButton.y == 2
    assert battleList.configureCreaturesButton.width == 12
    assert battleList.configureCreaturesButton.height == 12
    np.testing.assert_array_equal(battleList.configureCreaturesButton.image, configureCreaturesButton)
