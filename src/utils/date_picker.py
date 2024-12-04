from datetime import date
from nicegui import ui

class DatePicker:
    """DatePicker class consisting of an input field in which a date picker is implemented."""
    def __init__(self, default_date: date):
        self._date_input = None
        self._create_content(default_date)

    def _create_content(self, default_date: str):
        """Create ui content."""
        with ui.column().classes('space-y-4 w-full'):
            with ui.input('Date', value=default_date) as self._date_input:
                with ui.menu().props('no-parent-event') as menu:
                    with ui.date().bind_value(self._date_input):
                        with ui.row().classes('justify-end'):
                            ui.button('Close', on_click=menu.close).props('flat')
                with self._date_input.add_slot('append'):
                    ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

    def get_date(self) -> date:
        """Get date inputted into date picker object."""
        return self._date_input.value
