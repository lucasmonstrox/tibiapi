from typing import Optional
from tibiapi._common.rectImage.rectImage import RectImage
from .slot import Slot


class ActionBar:
    isLocked: bool
    lockButton: RectImage
    previousButton: RectImage
    nextButton: RectImage

    def getSlotByIndex(self, index: int) -> Optional[Slot]:
        return None

    def getSlotByHotkey(self, hotkey: str) -> Optional[Slot]:
        return None
