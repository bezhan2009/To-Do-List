import random
import string

from datagen.src.errors.generator_errors.errors import LenStringGetError


def generate_string(
        length: int,
        symbols_list: str = None
) -> str:
    """
    Get random string
    :param length: int: length of string
    :param symbols_list: str: list of symbols to generate string
    :return: str: random string
    """
    if not isinstance(length, int):
        raise ValueError("Length must be integer.")
    if length > 100000:
        raise LenStringGetError("Length cannot be greater than 100000.")
    elif length < 0:
        raise ValueError("Length must be positive.")

    if symbols_list is None:
        symbols_list = string.ascii_letters + string.digits + string.punctuation

    word = [random.choice(symbols_list) for _ in range(length)]
    word = ''.join(word)

    return word
