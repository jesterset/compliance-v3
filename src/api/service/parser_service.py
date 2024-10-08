from abc import ABC, abstractmethod
from typing import Any

# Define the abstract base class
class ParserService(ABC):
    @abstractmethod
    async def parse(self, obj: Any) -> Any:
        pass