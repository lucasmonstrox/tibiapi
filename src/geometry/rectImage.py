class RectImage:
    x: int
    y: int
    width: int
    height: int
    # TODO: add type
    image: any

    def __init__(self, x: int, y: int, image):
        self.x = x
        self.y = y
        self.width = len(image[0])
        self.height = len(image)
        self.image = image

    @staticmethod
    def makeFromRectImage(rectImage, x, y, width, height):
        return RectImage(x, y, rectImage.image[y:y + height, x: x + width])
