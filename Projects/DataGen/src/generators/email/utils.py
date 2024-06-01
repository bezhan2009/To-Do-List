import random
import string


def generate_string(length: int) -> str:
    """
    Generates a random string containing only lowercase letters.

    Args:
        length (int): The length of the generated string.

    Returns:
        str: The generated string.
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_string_with_digits(length: int, num_digits: int) -> str:
    """
    Generates a random string containing only lowercase letters followed by digits.

    Args:
        length (int): The length of the letter part of the string.
        num_digits (int): The number of digits to append at the end.

    Returns:
        str: The generated string with letters followed by digits.
    """
    letters_part = generate_string(length)
    digits_part = ''.join(random.choice(string.digits) for _ in range(num_digits))
    return letters_part + digits_part
