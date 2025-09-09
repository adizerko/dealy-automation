import random
from random import randint

from faker import Faker

from data import COUNTRY

faker = Faker('ru_RU')

class Generation:

    @staticmethod
    def first_name():
        name = faker.first_name()
        return name

    @staticmethod
    def last_name():
        return faker.last_name()

    @staticmethod
    def email():
        return faker.email()

    @staticmethod
    def password():
        length_password = randint(5,12)
        return faker.password(length=length_password)

    @staticmethod
    def company():
        return faker.company()

    @staticmethod
    def address():
        return faker.street_name()

    @staticmethod
    def address_complement():
        return faker.word()

    @staticmethod
    def postal_code():
        return random.randint(10000, 99999)

    @staticmethod
    def city():
        return faker.city_name()

    @staticmethod
    def country():
        return random.choice(COUNTRY)

    @staticmethod
    def phone():
        return faker.phone_number().replace(' ', '')
print(Generation.phone())

