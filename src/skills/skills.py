from src._common.container import Container
from src._common.rectImage import RectImage
from .utils import getNumberByImage


class Skills:
    cap: int
    food: int
    hp: int
    mana: int
    speed: int
    stamina: int
    offlineTraining: int
    magic: int
    fist: int
    club: int
    sword: int
    axe: int
    distance: int
    shielding: int
    fishing: int

    def __init__(self, rectImage: RectImage):
        self.container = Container(rectImage)

    # TODO: calculate thousand number when comma is present
    def getLevel(self) -> int:
        image = self.container.rectImage.image[26:34, :][:, :, 0]
        thousandNumberImage = image[:, 104:126]
        hundredNumberImage = image[:, 132:154]
        thousandNumber = getNumberByImage(thousandNumberImage) * 1000
        hundredNumber = getNumberByImage(hundredNumberImage)
        number = thousandNumber + hundredNumber
        return number
