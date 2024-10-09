from faker import Faker

fake = Faker()


def data_generate():
    user_data = {
        "email": f'test1234{fake.email()}',
        "password": fake.password(),
        "name": f'test1234{fake.name()}'
    }
    return user_data


def name_generator():
    generated_name = fake.user_name()
    return generated_name


def password_generator():
    generated_password = fake.password()
    return generated_password


def mail_generator():
    generate_mail = fake.email()
    return generate_mail


class InvalidUserData:
    invalid_data = [{'password': password_generator(), 'name': name_generator()},
                  {'email': mail_generator(), 'password': name_generator()},
                  {'email': mail_generator(), 'name': name_generator()}]


class SingleDataFiled:
    email = mail_generator()
    name = name_generator()
    password = password_generator()
