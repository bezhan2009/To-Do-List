import random
import string

from datagen.src.generators.string.generator import generate_string
from datagen.src.generators.url.dataclass import Url


def generate_url(
        length: int,
        protocol: str = "http"
) -> Url:
    """
    Generate random url
    :param length: int: length of url
    :param protocol: str: protocol of url
    :return: str: random url
    """
    if not isinstance(length, int):
        raise ValueError("Length must be integer.")
    elif length < 0:
        raise ValueError("Length must be positive.")

    if protocol not in ["http", "https"]:
        raise ValueError("Protocol must be http or https.")

    acceptable_symbols = string.ascii_letters + string.digits
    url = f"{protocol}://"
    protocol = url
    possible_domains = [".com", ".net", ".org", ".info", ".biz", ".ua", ".de", ".fr", ".it", ".es", ".pl", ".git"]
    selected_domain = random.choice(possible_domains)
    domain_length = length - len(url) - len(selected_domain)
    if domain_length < 0:
        raise ValueError("Length is too short for url.")
    address = generate_string(domain_length, acceptable_symbols)
    url += address
    url += selected_domain
    return Url(
        protocol,
        address,
        selected_domain
    )
