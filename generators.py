from faker import Faker
from random import randint

fake = Faker('ru_RU')


def fake_data():
    email = fake.email()
    password = fake.password(length=randint(6, 15), special_chars=False)
    name = fake.name()

    return email, password, name
