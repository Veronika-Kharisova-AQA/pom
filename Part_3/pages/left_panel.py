class LeftPanel:
    def __init__(self, app):
        self.app = app

    def open(self, category, item):
        print(f'Opening {category} -> {item}')

    def open_simple_registration_form(self):
        self.open('Element', 'Text Box')
