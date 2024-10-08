import falcon.asgi
from abc import ABC, abstractmethod

# Define the abstract base class
class BaseController(ABC):
    @abstractmethod
    def set_router(self, app: falcon.asgi.App):
        pass