import random

from datagen.src.generators.email.utils import generate_string_with_digits

try:
    from .dataclass import GeneratedEmail
except ImportError:
    from dataclass import GeneratedEmail


def generate_email(real_domain=True,
                   _domain: str = "",
                   _at: bool = True) -> GeneratedEmail:
    """
    Generates a random email address.

    Args:
        _at: if _at is set to True the generated email will be generated with this symbol "@".
        _domain: if _domain is empty, it will generate a random domain
        real_domain (bool): If True, use a real domain from a predefined list.
                            If False, generate a random domain.

    Returns:
        GeneratedEmail: An instance of GeneratedEmail containing the generated email.
    """
    real_domains = ["gmail.com", "outlook.com", "yahoo.com"]

    local_part = generate_string_with_digits(8, 4)  # 8 letters followed by 4 digits
    if _domain != "":
        if "." in _domain:
            domain = _domain
        elif ("." not in _domain) and (_at == False):
            domain = "." + _domain
        elif ("." not in _domain) and (_at == True):
            domain = _domain
    else:
        domain = f"{generate_string_with_digits(6, 0)}.{generate_string_with_digits(3, 0)}"
    if real_domain:
        domain = random.choice(real_domains)
    if _at:
        email = f"{local_part}@{domain}"
    else:
        email = f"{local_part}{domain}"
    return GeneratedEmail(email)


if __name__ == "__main__":
    print(generate_email(real_domain=True))
    print(generate_email(real_domain=False))
