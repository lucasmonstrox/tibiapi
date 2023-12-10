from bbox import BBox


def test_should_make_a_BBox():
    bbox = BBox(5, 10, 15, 20)
    assert bbox.x == 5
    assert bbox.y == 10
    assert bbox.width == 15
    assert bbox.height == 20
