# app/middleware.py
from starlette.middleware.base import BaseHTTPMiddleware

class LifespanMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, on_startup=None, on_shutdown=None):
        super().__init__(app)
        self.on_startup = on_startup
        self.on_shutdown = on_shutdown

    async def dispatch(self, request, call_next):
        if self.on_startup:
            await self.on_startup()
        response = await call_next(request)
        if self.on_shutdown:
            await self.on_shutdown()
        return response