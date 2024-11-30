# src/middleware.py
from nicegui import app
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    """Authentication Middleware Class"""
    def __init__(self, app, authenticator):
        super().__init__(app)
        self.authenticator = authenticator

    async def dispatch(self, request: Request, call_next):
        if not self.authenticator.is_authenticated() and request.url.path != "/login":
            app.storage.user["referrer_path"] = request.url.path
            return RedirectResponse("/login")
        return await call_next(request)
