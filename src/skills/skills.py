from src._common.container import Container
from src._common.rectImage import RectImage
from src.utils.color import isPixelColor
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

    def levelPercentageBarIsOpen(self) -> bool:
        return isPixelColor(self.container.rectImage.image[36, 9], (0, 0, 0))

    def getXp(self) -> int:
        y = 47 if self.levelPercentageBarIsOpen() else 40
        image = self.container.rectImage.image[y:y + 8, :][:, :, 0]
        hundredNumberImage = image[:, 132:154]
        hundredNumber = getNumberByImage(hundredNumberImage)
        thousandNumberImage = image[:, 104:126]
        thousandNumber = getNumberByImage(thousandNumberImage) * 1000
        millionNumberImage = image[:, 76:98]
        millionNumber = getNumberByImage(millionNumberImage) * 1000000
        billionNumberImage = image[:, 48:70]
        billionNumber = getNumberByImage(billionNumberImage) * 1000000000
        number = thousandNumber + hundredNumber + millionNumber + billionNumber
        return number
