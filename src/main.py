# src/main.py
import os
from nicegui import ui, app
from mongo_client import MongoDBClient
from authenticator import Authenticator
from middleware import AuthMiddleware
from pages.login_page import login_page
from pages.main_page import main_page

APP_SECRET = os.environ.get("APP_SECRET", "")
USERDB_DATABASE = os.environ.get("USERDB_DATABASE", "job_tracker")
USERDB_HOST = os.environ.get("USERDB_HOST", "application-database")
USERDB_PORT= int(os.environ.get("USERDB_PORT", "27017"))

user_db_client = MongoDBClient(USERDB_HOST, USERDB_PORT, USERDB_DATABASE)

authenticator = Authenticator(user_db_client)
app.add_middleware(AuthMiddleware, authenticator=authenticator)

@ui.page('/')
def main_page_route():
    """Route to main page."""
    main_page(authenticator)

@ui.page('/login')
def login_page_route():
    """Route to login page."""
    login_page(authenticator)

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=8050, reload=False, show=False, storage_secret=APP_SECRET)
