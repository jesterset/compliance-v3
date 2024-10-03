import falcon.asgi
from app.api.routes import register_routes
from app.core.config import Config, Environment

# Ensure that the config is loaded for the desired environment
# For example, loading DEV environment here. You can change this based on your needs.

config = Config.get_instance()

# Initialize Falcon app
app = falcon.asgi.App()

# Register routes
register_routes(app)
