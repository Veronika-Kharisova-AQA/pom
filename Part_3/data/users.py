from dataclasses import dataclass


@dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


student = SimpleUser(
    full_name='Veronika Kharisova',
    email='Veronika@example.com',
    current_address='Russia, Moscow',
    permanent_address='Russia, St.Petersburg'
)
