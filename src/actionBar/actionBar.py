from src._common.rectImage.rectImage import RectImage
from .slot import Slot


class ActionBar:
    isLocked: bool
    lockButton: RectImage
    previousButton: RectImage
    nextButton: RectImage

    def getSlotByIndex(self, index: int) -> Slot | None:
        return None

    def getSlotByHotkey(self, hotkey: str) -> Slot | None:
        return None
