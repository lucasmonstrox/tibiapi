import numpy as np
import pathlib
from src.battleList.battleList import BattleList
from src.geometry.rectImage import RectImage
from src.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_match_configure_creatures_button_image():
    battleListNotConfiguringImage = load(f'{currentPath}/battleListNotConfiguring.png')
    battleListRectImage = RectImage(0, 0, battleListNotConfiguringImage)
    battleList = BattleList(battleListRectImage)
    configureCreaturesButton = load('src/battleList/images/buttons/configureCreatures.png')
    np.testing.assert_array_equal(battleList.configureCreaturesButton.image, configureCreaturesButton)

def test_should_match_configure_creatures_button_pressed_image():
    battleListConfiguringImage = load(f'{currentPath}/battleListConfiguring.png')
    battleListRectImage = RectImage(0, 0, battleListConfiguringImage)
    battleList = BattleList(battleListRectImage)
    configureCreaturesButton = load('src/battleList/images/buttons/configureCreaturesPressed.png')
    np.testing.assert_array_equal(battleList.configureCreaturesButton.image, configureCreaturesButton)
