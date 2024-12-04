# src/pages/main_page.py
from nicegui import ui, app
from .tabs.application_form import JobApplicationTab
from .tabs.applications_overview import JobOverviewTab

def main_page(authenticator, application_db_client):
    """Main page accessible only after login."""
    def logout():
        authenticator.logout()
        ui.navigate.to('/login')

    with ui.header().classes(replace='row items-center bg-slate-700 h-16 pl-2 pr-2'):
        with ui.row().classes('flex-grow'):
            with ui.tabs().classes('flex') as tabs:
                ui.tab('Job Application')
                ui.tab('Job Overview')
                ui.tab('Extras')
        with ui.row().classes('items-center space-x-4'):
            ui.label(f"Welcome, @{app.storage.user.get('username')}!").classes('text-white')
            ui.button("Logout", on_click=logout).classes(
                'bg-red-500 text-white px-4 py-2 rounded'
            )

    with ui.tab_panels(tabs, value='Job Application').classes('w-full'):
        JobApplicationTab(application_db_client)
        JobOverviewTab(application_db_client)
