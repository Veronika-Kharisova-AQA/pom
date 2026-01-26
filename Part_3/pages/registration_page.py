from selene import browser, have, be

from Part_3.data.users import SimpleUser


class SimpleRegistrationPage:
    def __init__(self):
        self.field_full_name = browser.element('#userName')
        self.field_email = browser.element('#userEmail')
        self.field_current_address = browser.element('#currentAddress')
        self.field_permanent_address = browser.element('#permanentAddress')
        self.button_submit = browser.element('#submit')
        self.field_result = browser.element('.border')

    def open(self):
        browser.open('/text-box')
        return self

    def register(self, user: SimpleUser):
        self.field_full_name.type(user.full_name)
        self.field_email.type(user.email)
        self.field_current_address.type(user.current_address)
        self.field_permanent_address.type(user.permanent_address)
        browser.execute_script("arguments[0].scrollIntoView();", self.button_submit.locate())
        self.button_submit.click()

    def should_have_registered(self, user: SimpleUser):
        try:
            self.field_result.should(be.visible)

            self.field_result.should(have.text(
                f'Name:{user.full_name}\n'
                f'Email:{user.email}\n'
                f'Current Address :{user.current_address}\n'
                f'Permananet Address :{user.permanent_address}'
            ))
        finally:
            browser.config.timeout = 10
