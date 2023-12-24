from .message import Message


class Tab:
    name: str
    index: int

    def hasNewMessages(self) -> bool:
        return True

    def visibleMessages(self) -> list[Message]:
        return []
