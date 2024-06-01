import random
import string

try:
    from .dataclass import PhoneNumber
except ImportError:
    from dataclass import PhoneNumber


def generate_phone_numbers(country_code: int, number_count: int = 1, phone_length: int = 10) -> list[PhoneNumber]:
    """
    Generates a list of random phone numbers for a given country code.

    :param country_code: The country code for the phone numbers.
    :param number_count: The number of phone numbers to generate. Default is 1.
    :param phone_length: The length of the phone number without the country code. Default is 10.
    :return: A list of generated PhoneNumber objects.
    """
    if country_code <= 0:
        raise ValueError("Invalid country code. Please provide a positive integer for the country code.")
    if number_count <= 0:
        raise ValueError("Invalid number count. Please provide a positive integer for the number count.")
    if phone_length <= 0:
        raise ValueError("Invalid phone length. Please provide a positive integer for the phone length.")

    generated_phone_numbers = []

    for _ in range(number_count):
        number = ''.join(random.choice(string.digits) for _ in range(phone_length))
        generated_phone_numbers.append(PhoneNumber(country_code, number))

    return generated_phone_numbers
