from functools import cached_property
from tibiapi._common.rectImage import RectImage
from .utils import healthPercentage, manaPercentage


class StatusBar:
    def __init__(self, rectImage: RectImage):
        self.rectImage = rectImage

    @cached_property
    def healthPercentage(self) -> int:
        return healthPercentage(self.rectImage.image[5:6, 13:, :][0])

    @cached_property
    def manaPercentage(self) -> int:
        return manaPercentage(self.rectImage.image[18:19, 13:, :][0])
