import falcon.asgi
from app.api.routes import register_routes
from app.core.config import Config, Environment

config = Config.get_instance()

app = falcon.asgi.App()

register_routes(app)
