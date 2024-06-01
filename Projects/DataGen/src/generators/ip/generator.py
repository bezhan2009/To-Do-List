import random

from datagen.src.generators.ip.dataclass import Ip


def ipv4_generate(
        valid: bool = True
) -> str:
    """
    Generate random ipv4 address
    :param valid: bool: valid or invalid ip
    :return: str: ipv4 address
    """
    if valid:
        ip_string = ".".join(str(random.randint(0, 255)) for _ in range(4))
        return Ip(ip_string)
    else:
        ip_string = ".".join(str(random.randint(255, 999)) for _ in range(4))
        return Ip(ip_string)


def ipv6_generate(
        valid: bool = True
) -> str:
    """
    Generate random ipv6 address
    :param valid: bool: valid or invalid ip
    :return: str: ipv6 address
    """
    if valid:
        ip_string = ":".join("".join(random.choices("0123456789abcdef", k=4)) for _ in range(8))
        return Ip(ip_string)
    else:
        ip_string = ":".join("".join(random.choices("ghijklmnopqrstuvwxyz", k=4)) for _ in range(8))
        return Ip(ip_string)
