# src/pages/main_page.py
from nicegui import ui, app

def main_page(authenticator):
    """Main page accessible only after login."""
    def logout():
        authenticator.logout()
        ui.navigate.to('/login')

    with ui.card().classes("absolute-center"):
        ui.label(f"Welcome, {app.storage.user.get('username', 'Guest')}!").classes("text-2xl")
        ui.button("Logout", on_click=logout)
