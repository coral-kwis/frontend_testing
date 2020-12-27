import random
import string
from datetime import datetime, timedelta


def generate_random_string(string_length):
    return ''.join(random.choices(string.ascii_letters, k=string_length))


def generate_random_number(end, start_index=0):
    return random.randint(start_index, end)


def generate_random_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = 'coral.com'
    if not email_prefix:
        email_prefix = 'test'
    email_length = random.randint(1, 20)
    random_email_string = ''.join(random.choices(string.ascii_letters + string.digits, k=email_length))
    email = email_prefix + '_' + random_email_string + '@' + domain
    password_length = random.randint(8, 20)
    password = ''.join(random.choices(string.ascii_letters, k=password_length))
    return {'email': email, 'password': password}

