from functools import cached_property
from src._common.container import TopBar as ContainerTopBar
from src._common.rectImage import makeFromRectImage, RectImage


class TopBar(ContainerTopBar):
    @cached_property
    def openSecondaryBattleListButton(self) -> RectImage:
        return makeFromRectImage(self.rectImage, 109, 2, 12, 12)

    @cached_property
    def configureButton(self) -> RectImage:
        return makeFromRectImage(self.rectImage, 121, 2, 12, 12)

    @cached_property
    def configureCreaturesButton(self) -> RectImage:
        return makeFromRectImage(self.rectImage, 133, 2, 12, 12)
