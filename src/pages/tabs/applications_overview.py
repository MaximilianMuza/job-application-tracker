# src/pages/tabs/application_overview.py
from nicegui import ui
from nicegui.elements.tabs import TabPanel

class JobOverviewTab(TabPanel):
    """Provides an overview of submitted job applications."""
    def __init__(self, application_db_client):
        super().__init__(name="Job Overview")
        self._application_db_client = application_db_client
        self._create_tab_content()
        self._load_applications()

    def _create_tab_content(self):
        """Create tab content"""
        with self:
            ui.label('Applications Overview').classes('text-lg font-bold mb-4')

    def _load_applications(self):
        """Load applications"""
        self._application_db_client.get_applications()
