from typing import Optional


class Slot:
    available: bool
    equipped: bool
    hotkey: Optional[str]
    count: Optional[int]
