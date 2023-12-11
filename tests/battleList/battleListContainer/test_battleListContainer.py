import pathlib
from src.battleList.battleListContainer import BattleListContainer
from src.geometry.rectImage import RectImage
from src.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_method_isConfiguringCreatures_return_True_when_configuring_creatures_is_shown():
    image = load(f'{currentPath}/battleListConfiguring.png')
    rectImage = RectImage(0, 0, image)
    battleListContainer = BattleListContainer(rectImage)
    assert battleListContainer.isConfiguringCreatures() == True


def test_should_method_isConfiguringCreatures_return_False_when_configuring_creatures_is_not_shown():
    image = load(f'{currentPath}/battleListNotConfiguring.png')
    rectImage = RectImage(0, 0, image)
    battleListContainer = BattleListContainer(rectImage)
    assert battleListContainer.isConfiguringCreatures() == False
