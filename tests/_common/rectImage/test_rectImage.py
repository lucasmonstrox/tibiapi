import pathlib
from src._common.rectImage import RectImage
from src.utils.image import load


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_make_a_RectImage():
    image = load(f'{currentPath}/battleList.png')
    rectImage = RectImage(5, 10, image)
    assert rectImage.x == 5
    assert rectImage.y == 10
    assert rectImage.width == 176
    assert rectImage.height == 19
