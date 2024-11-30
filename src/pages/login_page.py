# src/pages/login_page.py
from nicegui import ui

def login_page(authenticator):
    """Login and Registration Page with Tabs."""
    def try_login():
        if authenticator.login(username.value, password.value):
            ui.notify("Login successful!", color="positive")
            ui.navigate.to("/")
        else:
            ui.notify("Invalid username or password", color="negative")

    def try_register():
        if authenticator.register(username.value, password.value):
            ui.notify("Registration successful. Please log in!", color="positive")
        else:
            ui.notify("Username already exists.", color="negative")

    with ui.card().classes('absolute-center'):
        username = ui.input("Username").props("outlined")
        password = ui.input("Password", password=True).props("outlined")
        with ui.row():
            ui.button("Log in", on_click=try_login)
            ui.button("Register", on_click=try_register)
