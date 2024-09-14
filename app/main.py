# app/main.py
import falcon.asgi
from app.api.routes import register_routes
from app.core.elastic import ElasticClient

client = ElasticClient.get_client()

app = falcon.asgi.App()

register_routes(app)