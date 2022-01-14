from typing import Any, Optional


class Payment_Method:
    def __init__(self, name: str, enabled: bool, id: Optional[int] = None):
        self.id = id
        self.name = name
        self.enabled = enabled