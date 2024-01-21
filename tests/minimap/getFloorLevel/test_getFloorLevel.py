import os
from tibiapi._common.rectImage import RectImage
from tibiapi.minimap import Minimap
from tibiapi.utils.image import load


def loadMinimapByImage(imagePath: str) -> Minimap:
    currentPath = os.path.dirname(os.path.abspath(__file__))
    minimapImage = load(f'{currentPath}/images/{imagePath}')
    minimapRectImage = RectImage(0, 0, minimapImage)
    return Minimap(minimapRectImage)


def test_should_return_0():
    minimap = loadMinimapByImage('minimapWithFloorLevel0.png')
    assert minimap.getFloorLevel() == 0


def test_should_return_1():
    minimap = loadMinimapByImage('minimapWithFloorLevel1.png')
    assert minimap.getFloorLevel() == 1


def test_should_return_2():
    minimap = loadMinimapByImage('minimapWithFloorLevel2.png')
    assert minimap.getFloorLevel() == 2


def test_should_return_3():
    minimap = loadMinimapByImage('minimapWithFloorLevel3.png')
    assert minimap.getFloorLevel() == 3


def test_should_return_4():
    minimap = loadMinimapByImage('minimapWithFloorLevel4.png')
    assert minimap.getFloorLevel() == 4


def test_should_return_5():
    minimap = loadMinimapByImage('minimapWithFloorLevel5.png')
    assert minimap.getFloorLevel() == 5


def test_should_return_6():
    minimap = loadMinimapByImage('minimapWithFloorLevel6.png')
    assert minimap.getFloorLevel() == 6


def test_should_return_7():
    minimap = loadMinimapByImage('minimapWithFloorLevel7.png')
    assert minimap.getFloorLevel() == 7


def test_should_return_8():
    minimap = loadMinimapByImage('minimapWithFloorLevel8.png')
    assert minimap.getFloorLevel() == 8


def test_should_return_9():
    minimap = loadMinimapByImage('minimapWithFloorLevel9.png')
    assert minimap.getFloorLevel() == 9


def test_should_return_10():
    minimap = loadMinimapByImage('minimapWithFloorLevel10.png')
    assert minimap.getFloorLevel() == 10


def test_should_return_11():
    minimap = loadMinimapByImage('minimapWithFloorLevel11.png')
    assert minimap.getFloorLevel() == 11


def test_should_return_12():
    minimap = loadMinimapByImage('minimapWithFloorLevel12.png')
    assert minimap.getFloorLevel() == 12


def test_should_return_13():
    minimap = loadMinimapByImage('minimapWithFloorLevel13.png')
    assert minimap.getFloorLevel() == 13


def test_should_return_14():
    minimap = loadMinimapByImage('minimapWithFloorLevel14.png')
    assert minimap.getFloorLevel() == 14


def test_should_return_15():
    minimap = loadMinimapByImage('minimapWithFloorLevel15.png')
    assert minimap.getFloorLevel() == 15
