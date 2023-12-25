from datetime import time
from typing import Optional


class Message:
    content: str
    date: time
    creatureName: Optional[str]
