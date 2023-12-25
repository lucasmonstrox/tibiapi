from typing import Optional
from .cooldown import Cooldown


class CooldownBar:
    def getCooldownByIndex(self, index: int) -> Optional[Cooldown]:
        return None

    def getCooldownByName(self, name: str) -> Optional[Cooldown]:
        return None
