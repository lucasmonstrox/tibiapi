import pathlib
from tibiapi._common.rectImage import RectImage
from tibiapi.battleList import BattleList
from tibiapi.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_True_when_configuring_creatures_is_shown():
    battleListImage = load(
        f'{currentPath}/images/battleListConfiguringCreatures.png')
    rectImage = RectImage(0, 0, battleListImage)
    battleList = BattleList(rectImage)
    assert battleList.isConfiguringCreatures == True


def test_should_return_False_when_configuring_creatures_is_not_shown():
    battleListImage = load(
        f'{currentPath}/images/battleListNotConfiguringCreatures.png')
    rectImage = RectImage(0, 0, battleListImage)
    battleList = BattleList(rectImage)
    assert battleList.isConfiguringCreatures == False
