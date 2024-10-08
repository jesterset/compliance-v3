from typing import Any, Dict, Type
from api.service.parser_service import ParserService

# Define the ParserHandler class
class ParserHandler:
    def __init__(self):
        self.parser_services: Dict[str, ParserService] = {}

    def register_parser_service(self, parser_service_name: str, parser_service: Type[ParserService]) -> None:
        self.parser_services[parser_service_name] = parser_service

    async def parse(self, obj: Any, parser_service_name: str) -> Any:
        parser = self.parser_services.get(parser_service_name)
        if parser:
            return await parser.parse(obj)
        else:
            raise ValueError('Unsupported parser method')