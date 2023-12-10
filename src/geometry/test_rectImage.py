from rectImage import RectImage


def test_should_make_a_RectImage():
    rectImage = RectImage(5, 10, 15, 20)
    assert rectImage.x == 5
    assert rectImage.y == 10
    assert rectImage.width == 15
    assert rectImage.height == 20
