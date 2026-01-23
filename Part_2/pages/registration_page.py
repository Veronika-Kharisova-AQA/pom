from pathlib import Path

from selene import browser, have, command


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user):
        # name
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)

        # email
        browser.element('#userEmail').type(user.email)

        # gender
        browser.all('.custom-control-label').element_by(
            have.exact_text(user.gender)
        ).click()

        # phone
        browser.element('#userNumber').type(user.phone)

        # date of birth
        browser.element('#dateOfBirthInput').click()

        # month
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').all('option').element_by(
            have.exact_text(user.birth_month)
        ).click()

        # year
        browser.element('.react-datepicker__year-select').click()
        browser.element(
            f'.react-datepicker__year-select option[value="{user.birth_year}"]'
        ).click()

        # day
        browser.all('.react-datepicker__day').element_by(
            have.exact_text(user.birth_day)
        ).click()

        # subject
        browser.element('#subjectsInput').type(user.subject).press_enter()

        # hobby
        browser.element('#hobbiesWrapper').perform(command.js.scroll_into_view)
        browser.all('[for^="hobbies-checkbox"]').element_by(have.text(user.hobby)).click()

        # picture
        picture = str(
            Path(__file__).parent.parent.joinpath('resources', user.picture).resolve()
        )
        browser.element('#uploadPicture').set_value(picture)

        # address
        browser.element('#currentAddress').type(user.address)

        # state
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option"]').element_by(
            have.text(user.state)
        ).click()

        # city
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option"]').element_by(
            have.text(user.city)
        ).click()

        # submit
        browser.element('#submit').click()

        return self

    def should_have_registered(self, user):
        results = browser.element('.table-responsive')

        results.should(have.text(f'{user.first_name} {user.last_name}'))
        results.should(have.text(user.email))
        results.should(have.text(user.gender))
        results.should(have.text(user.phone))
        results.should(have.text(f'{user.birth_day} {user.birth_month},{user.birth_year}'))
        results.should(have.text(user.subject))
        results.should(have.text(user.hobby))
        results.should(have.text(user.picture))
        results.should(have.text(user.address))
        results.should(have.text(f'{user.state} {user.city}'))

        return self