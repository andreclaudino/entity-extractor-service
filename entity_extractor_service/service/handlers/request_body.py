from dataclasses import dataclass, field
from typing import List, Optional, Set

@dataclass
class RequestBody:
    text: str
    labels: Set[str]
    threshold: float = field(default=0.5)


    def check_errors(self) -> Optional[List[str]]:
        error_messages = []

        if not self.text:
            error_messages.append("text field cannot be empty")
        if not self.labels:
            error_messages.append("lables field cannot be empty")

        if error_messages:
            return error_messages
        else:
            return None
    
    def __dict__(self) -> dict:
        return dict(text=self.text, labels=self.labels, threshold=self.threshold)

    def __str__(self) -> str:
        return "{}".format(self.__dict__)
