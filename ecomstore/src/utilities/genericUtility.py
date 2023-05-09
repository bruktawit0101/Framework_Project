
import random
import string
import logging as logger


def generate_random_email_and_password(email_prefix='supersql', domain='gmail.com', elength=10):
    '''

    Generates a randome email and password combination.
    :param email_prefix:
    :param domain:
    :return: dictionary - A dictionary with keys 'email' and 'password'
    '''

    random_letters = ''.join(random.choices(string.ascii_lowercase, k=elength))
    email = f"{email_prefix}_{random_letters}@{domain}"

    length_of_password = 20
    random_password = ''.join(random.choices(string.ascii_lowercase, k=length_of_password))
    random_info = {"email": email, "password": random_password}
    logger.debug(f"randomly generated email and password: {random_info}")
    return random_info

if __name__ == '__main__':
    generate_random_email_and_password()

