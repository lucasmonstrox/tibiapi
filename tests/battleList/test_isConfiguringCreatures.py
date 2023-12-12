import pathlib
from src.battleList.battleList import BattleList
from src.geometry.rectImage import RectImage
from src.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_True_when_configuring_creatures_is_shown():
    image = load(f'{currentPath}/images/battleListConfiguring.png')
    rectImage = RectImage(0, 0, image)
    battleList = BattleList(rectImage)
    assert battleList.isConfiguringCreatures == True

def test_should_return_False_when_configuring_creatures_is_not_shown():
    image = load(f'{currentPath}/images/battleListNotConfiguring.png')
    rectImage = RectImage(0, 0, image)
    battleList = BattleList(rectImage)
    assert battleList.isConfiguringCreatures == False
