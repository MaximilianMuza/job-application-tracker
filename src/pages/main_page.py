# src/pages/main_page.py
from nicegui import ui, app
from pages.tabs import add_application_tab, applications_overview_tab, extras_tab

def main_page(authenticator):
    """Main page accessible only after login."""
    def logout():
        authenticator.logout()
        ui.navigate.to('/login')

    with ui.header().classes(replace='row items-center bg-slate-700 h-16 pl-2 pr-2'):
        with ui.row().classes('flex-grow'):
            with ui.tabs().classes('flex') as tabs:
                ui.tab('Add Application')
                ui.tab('Applications Overview')
                ui.tab('Extras')
        with ui.row().classes('items-center space-x-4'):
            ui.label(f"Welcome, {app.storage.user.get('username', 'Guest')}!").classes('text-white')
            ui.button("Logout", on_click=logout).classes(
                'bg-red-500 text-white px-4 py-2 rounded'
            )

    with ui.tab_panels(tabs, value='Add Application').classes('w-full'):
        add_application_tab()
        applications_overview_tab()
        extras_tab()
