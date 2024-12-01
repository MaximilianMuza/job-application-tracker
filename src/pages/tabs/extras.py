# src/pages/tabs/extras.py
from nicegui import ui

def extras_tab():
    """Extras tab"""
    with ui.tab_panel('Extras'):
        ui.label('Extras').classes('text-lg font-bold mb-4')
