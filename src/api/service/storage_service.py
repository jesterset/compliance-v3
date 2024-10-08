from abc import ABC, abstractmethod
from typing import Any, Dict

# Define the abstract base class
class StorageService(ABC):
    @abstractmethod
    def config(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def write(self, index: str, obj: Any) -> None:
        pass