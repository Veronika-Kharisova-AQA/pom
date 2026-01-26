from Part_3.pages.left_panel import LeftPanel
from Part_3.pages.registration_page import SimpleRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.simple_registration = SimpleRegistrationPage()
        self.left_panel = LeftPanel(self)

app = ApplicationManager()