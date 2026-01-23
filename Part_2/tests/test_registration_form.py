from Part_2.models.user import User
from Part_2.pages.registration_page import RegistrationPage


def test_registration_form():
    user = User(
        first_name='Veronika',
        last_name='Kharisova',
        email='Veronika@example.com',
        gender='Female',
        phone='5643782341',
        birth_day='14',
        birth_month='July',
        birth_year='2002',
        subject='Maths',
        hobby='Sports',
        picture='cat.jpg',
        address='Russia, Moscow',
        state='NCR',
        city='Delhi'
    )

    page = RegistrationPage()

    page.open()
    page.register(user)
    page.should_have_registered(user)

