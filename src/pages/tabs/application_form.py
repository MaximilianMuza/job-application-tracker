# src/pages/tabs/add_application.py
from datetime import datetime, date
import logging
from nicegui import ui
from nicegui.elements.tabs import TabPanel

from applications import Application
from utils import DatePicker

class JobApplicationTab(TabPanel):
    """Handles uploading and storing job application information."""
    def __init__(self, application_db_client):
        super().__init__(name="Job Application")
        self._application_db_client = application_db_client
        self._create_tab_content()

    def _create_tab_content(self):
        """Create tab content."""
        with self:
            ui.label('Add a New Application').classes('text-lg font-bold mb-4')

            date_input = DatePicker(date.today())
            job_title_input = ui.input('Job Title').classes('w-full')
            company_name_input = ui.input('Company').classes('w-full')
            job_posting_url_input = ui.input('Link to Job Posting').classes('w-full')
            file_link_input = ui.input("File Link").classes('w-full')
            description_input = ui.textarea('Description').classes('w-full h-32')

            ui.button(
                text='Submit',
                on_click=lambda: self._submit_form(
                    date_input.get_date(),
                    job_title_input.value,
                    company_name_input.value,
                    job_posting_url_input.value,
                    description_input.value,
                    file_link_input.value
                )
            ).classes('bg-blue-500 text-white px-4 py-2 rounded')

    def _validate_inputs(self, job_title: str, company_name: str, job_posting_url: str):
        """Validate form inputs"""
        if job_title == "":
            raise ValueError("Job title is not specified.")
        if company_name == "":
            raise ValueError("Company name is not specified.")
        if job_posting_url == "":
            raise ValueError("Link to job posting is not specified.")

    def _submit_form(
        self,
        date: datetime.date,
        job_title: str,
        company_name: str,
        job_posting_url: str,
        file_link: str,
        description: str
    ):
        """Submit job application form"""
        try:
            self._validate_inputs(job_title, company_name, job_posting_url)

            application = Application(
                date=date,
                job_title=job_title,
                company_name=company_name,
                job_posting_url=job_posting_url,
                file_link=file_link,
                description=description
            )
            self._application_db_client.insert_application(application)
        except ValueError as e:
            logging.error(e)
            ui.notify(e, type="warning")
        else:
            ui.notify(f'Application with uuid {application.uuid} submitted.', type='positive')
