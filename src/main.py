# src/main.py
import os
from nicegui import ui, app
from mongo_client import MongoDBClient
from authenticator import Authenticator
from middleware import AuthMiddleware
from pages.login_page import login_page
from pages.main_page import main_page

APP_PORT=3080
MONGODB_DATABASE="job_tracker"
MONGODB_HOST="localhost"
MONGODB_PORT=27017
SECRET_KEY = "CHANGE_THIS_SECRET"


mongo_client = MongoDBClient(MONGODB_HOST, MONGODB_PORT, MONGODB_DATABASE)
users_collection = mongo_client.get_collection("users")

authenticator = Authenticator(users_collection)
app.add_middleware(AuthMiddleware, authenticator=authenticator)

@ui.page('/')
def main_page_route():
    main_page(authenticator)

@ui.page('/login')
def login_page_route():
    ui.timer(60, lambda: ui.notify("Heartbeat message"))
    login_page(authenticator)

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=APP_PORT, reload=False, show=False, storage_secret=SECRET_KEY)
