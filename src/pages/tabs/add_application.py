# src/pages/tabs/add_application.py
from nicegui import ui
from datetime import date

def add_application_tab():
    with ui.tab_panel('Add Application'):
        ui.label('Add a New Application').classes('text-lg font-bold mb-4')

        with ui.column().classes('space-y-4 w-full'):
            with ui.input('Date', value=date.today()) as date_field:
                with ui.menu().props('no-parent-event') as menu:
                    with ui.date().bind_value(date_field):
                        with ui.row().classes('justify-end'):
                            ui.button('Close', on_click=menu.close).props('flat')
                with date_field.add_slot('append'):
                    ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

            job_title_input = ui.input('Job Title').classes('w-full')
            company_input = ui.input('Company').classes('w-full')
            description_input = ui.textarea('Description').classes('w-full h-32')

            ui.button(
                'Submit',
                on_click=lambda: submit_form(date_field, job_title_input, company_input, description_input)
            ).classes('bg-blue-500 text-white px-4 py-2 rounded')

def submit_form(date_input, job_title_input, company_input, description_input):
    data = {
        'Date': date_input.value,
        'Job Title': job_title_input.value,
        'Company': company_input.value,
        'Description': description_input.value,
    }
    ui.notify(f'Form submitted with data: {data}', color='success')
