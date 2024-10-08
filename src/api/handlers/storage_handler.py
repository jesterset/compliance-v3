from typing import Any, Dict, Type
from api.service.storage_service import StorageService

# Define the StorageHandler class
class StorageHandler:
    def __init__(self):
        self.storage_services: Dict[str, StorageService] = {}

    def register_storage_service(self, storage_service_name: str, storage_service: Type[StorageService]) -> None:
        self.storage_services[storage_service_name] = storage_service

    async def write(self, storage_service_name: str, index: str, obj: Any) -> None:
        storage = self.storage_services.get(storage_service_name)
        if storage:
            await storage.write(index, obj)
        else:
            raise ValueError('Unsupported storage option')