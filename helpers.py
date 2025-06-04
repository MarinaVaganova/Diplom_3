from faker import Faker


fake = Faker()
fakeRU = Faker(locale='ru_RU')

def create_random_email():
    email = f'marina_20_{fake.email()}'
    return email

def create_random_password():
    password = fake.password()
    return password

def create_random_name():
    name = fakeRU.first_name()
    return name