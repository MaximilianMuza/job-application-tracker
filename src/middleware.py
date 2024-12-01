# src/middleware.py
from nicegui import app
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    """Authentication middleware to ensure that the user is authenticated
    before accessing certain routes.

    This middleware intercepts requests and checks whether the user is authenticated.
    If the user is not authenticated and is trying to access a protected route (i.e., not 
    "/login"), they will be redirected to the login page. If the user is authenticated, 
    the request is passed to the next handler.
    """
    def __init__(self, app, authenticator):
        """Initializes the middleware with the given application and authenticator.

        Args:
            app (FastAPI app): The FastAPI application instance.
            authenticator (Authenticator): The authenticator instance used to verify authentication.
        """
        super().__init__(app)
        self.authenticator = authenticator

    async def dispatch(self, request: Request, call_next):
        """Intercepts the request to check if the user is authenticated. If not authenticated,
        the user will be redirected to the login page.

        Args:
            request (Request): The incoming request object.
            call_next (Callable): The next middleware or route handler to call.

        Returns:
            Response: The response from either the next handler or a RedirectResponse.
        """
        if request.url.path.startswith("/_nicegui") or request.url.path.startswith("/static"):
            return await call_next(request)

        if not self.authenticator.is_authenticated() and request.url.path != "/login":
            app.storage.user["referrer_path"] = request.url.path  # Save requested path
            return RedirectResponse("/login")

        return await call_next(request)
