from werkzeug.security import generate_password_hash, check_password_hash
from nicegui import app


class Authenticator:
    """Authenticator Class"""
    def __init__(self, user_collection):
        self.user_collection = user_collection

    def login(self, username, password):
        """Authenticate a user and set the session."""
        user = self.user_collection.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            app.storage.user.update({"username": username, "authenticated": True})
            return True
        return False

    def register(self, username, password):
        """Register a new user."""
        if self.user_collection.find_one({"username": username}):
            return False  # Username already exists
        hashed_password = generate_password_hash(password)
        self.user_collection.insert_one({"username": username, "password": hashed_password})
        return True

    def is_authenticated(self):
        """Check if the user is logged in."""
        return app.storage.user.get("authenticated", False)

    def logout(self):
        """Clear user session."""
        app.storage.user.clear()
