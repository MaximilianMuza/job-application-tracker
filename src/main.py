# src/main.py
import os
from nicegui import ui, app
from utils.mongo_client import UserDBClient, ApplicationDBClient
from utils.authenticator import Authenticator
from utils.middleware import AuthMiddleware
from pages.login_page import login_page
from pages.main_page import main_page

APP_NAME = os.environ.get("APP_NAME", "JobTracker")
APP_SECRET = os.environ.get("APP_SECRET", "")
USERDB_DATABASE = os.environ.get("USERDB_DATABASE", "users_database")
USERDB_HOST = os.environ.get("USERDB_HOST", "job-tracker-db")
USERDB_PORT= int(os.environ.get("USERDB_PORT", "27017"))
APPLICATIONDB_DATABASE = os.environ.get("APPLICATIONDB_DATABASE", "applications_database")
APPLICATIONDB_HOST = os.environ.get("APPLICATIONDB_HOST", "job-tracker-db")
APPLICATIONDB_PORT = int(os.environ.get("APPLICATIONDB_PORT", "271017"))

user_db_client = UserDBClient(USERDB_HOST, USERDB_PORT, USERDB_DATABASE)
application_db_client = ApplicationDBClient(APPLICATIONDB_HOST, APPLICATIONDB_PORT, APPLICATIONDB_DATABASE)

authenticator = Authenticator(user_db_client)
app.add_middleware(AuthMiddleware, authenticator=authenticator)

@ui.page('/')
def main_page_route():
    """Route to main page."""
    main_page(authenticator, application_db_client)

@ui.page('/login')
def login_page_route():
    """Route to login page."""
    login_page(authenticator)

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title=APP_NAME, port=8050, reload=False, show=False, storage_secret=APP_SECRET)
