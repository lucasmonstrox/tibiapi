import numpy as np
import os
from tibiapi._common.rectImage import RectImage
from tibiapi.battleList import BattleList
from tibiapi.utils.image import load


currentPath = os.path.dirname(os.path.abspath(__file__))


def test_should_return_None_when_battle_list_is_minimized():
    battleListImage = load(f'{currentPath}/images/battleListMinimized.png')
    battleListRectImage = RectImage(0, 0, battleListImage)
    battleList = BattleList(battleListRectImage)
    assert battleList.togglePlayersButton is None


def test_should_return_None_when_not_configuring_creatures():
    battleListImage = load(
        f'{currentPath}/images/battleListNotConfiguringCreatures.png')
    battleListRectImage = RectImage(0, 0, battleListImage)
    battleList = BattleList(battleListRectImage)
    assert battleList.togglePlayersButton is None


def test_should_return_hidePlayersButton_when_configuring_creatures():
    battleListImage = load(
        f'{currentPath}/images/battleListConfiguringCreatures.png')
    battleListRectImage = RectImage(0, 0, battleListImage)
    battleList = BattleList(battleListRectImage)
    hidePlayersButtonImage = load(
        'tibiapi/battleList/images/buttons/hidePlayers.png')
    assert battleList.togglePlayersButton.x == 23
    assert battleList.togglePlayersButton.y == 17
    assert battleList.togglePlayersButton.width == 20
    assert battleList.togglePlayersButton.height == 20
    np.testing.assert_array_equal(
        battleList.togglePlayersButton.image, hidePlayersButtonImage)


def test_should_return_showPlayersButton_when_configuring_creatures():
    battleListImage = load(
        f'{currentPath}/images/battleListConfigureCreaturesWithButtonsNotPressed.png')
    battleListRectImage = RectImage(0, 0, battleListImage)
    battleList = BattleList(battleListRectImage)
    showPlayersButtonImage = load(
        'tibiapi/battleList/images/buttons/showPlayers.png')
    assert battleList.togglePlayersButton.x == 23
    assert battleList.togglePlayersButton.y == 17
    assert battleList.togglePlayersButton.width == 20
    assert battleList.togglePlayersButton.height == 20
    np.testing.assert_array_equal(
        battleList.togglePlayersButton.image, showPlayersButtonImage)
