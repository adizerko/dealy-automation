from random import randint

from faker import Faker

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

