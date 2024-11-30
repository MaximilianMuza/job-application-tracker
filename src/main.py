# src/main.py
import os
from nicegui import ui, app
from mongo_client import MongoDBClient
from authenticator import Authenticator
from middleware import AuthMiddleware
from pages.login_page import login_page
from pages.main_page import main_page

MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE", "job_tracker")
MONGODB_HOST = os.environ.get("MONGODB_HOST", "application-database")
MONGODB_PORT= int(os.environ.get("MONGODB_PORT", 27017))
SECRET_KEY = os.environ.get("SECRET_KEY", "")


mongo_client = MongoDBClient(MONGODB_HOST, MONGODB_PORT, MONGODB_DATABASE)
users_collection = mongo_client.get_collection("users")

authenticator = Authenticator(users_collection)
app.add_middleware(AuthMiddleware, authenticator=authenticator)

@ui.page('/')
def main_page_route():
    main_page(authenticator)

@ui.page('/login')
def login_page_route():
    login_page(authenticator)

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=8050, reload=False, show=False, storage_secret=SECRET_KEY)
