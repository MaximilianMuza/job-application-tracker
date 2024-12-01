# src/pages/tabs/application_overview.py
from nicegui import ui

def applications_overview_tab():
    """Application overview tab"""
    with ui.tab_panel('Applications Overview'):
        ui.label('Applications Overview').classes('text-lg font-bold mb-4')
