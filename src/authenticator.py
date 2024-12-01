# src/authenticator.py
from werkzeug.security import generate_password_hash, check_password_hash
from nicegui import app

from mongo_client import UserDBClient

class Authenticator:
    """Handles user authentication and session management.

    The Authenticator class provides methods for logging in, registering, checking 
    authentication status, and logging out users. It interacts with the `UserDBClient` 
    to perform necessary database operations for user management (like finding and inserting users).
    """
    def __init__(self, user_db_client: UserDBClient):
        self.user_db_client = user_db_client

    def login(self, username, password) -> bool:
        """Authenticates a user by checking the provided username and password.

        This method verifies the credentials by fetching the user from the database 
        and comparing the hashed password with the one stored in the database. If the 
        credentials are correct, the user's session is set, marking them as authenticated.

        Args:
            username (str): The username of the user attempting to log in.
            password (str): The password provided by the user.

        Returns:
            bool: `True` if the login is successful, `False` otherwise.
        """
        user = self.user_db_client.find_user(username)
        if user and check_password_hash(user["password"], password):
            app.storage.user.update({"username": username, "authenticated": True})
            return True
        return False

    def register(self, username, password) -> bool:
        """Registers a new user by adding them to the database.

        Args:
            username (str): The username the new user wants to register.
            password (str): The password the new user wants to register with.

        Returns:
            bool: `True` if the registration is successful, `False` if the username already exists.
        """
        if self.user_db_client.find_user(username):
            return False  # Username already exists
        hashed_password = generate_password_hash(password)
        self.user_db_client.insert_user(username, hashed_password)
        return True

    def is_authenticated(self) -> bool:
        """Checks whether the user is currently authenticated.

        Returns:
            bool: `True` if the user is authenticated, `False` otherwise.
        """
        return app.storage.user.get("authenticated", False)

    def logout(self):
        """Logs out the current user by clearing their session."""
        app.storage.user.clear()
