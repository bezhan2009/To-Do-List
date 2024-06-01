class PhoneNumber:
    """
    Represents a phone number with a country code and number.

    Attributes:
        country_code (int): The country code of the phone number.
        number (str): The phone number.
    """

    def __init__(self, country_code: int, number: str) -> None:
        self.country_code: int = country_code
        self.number: str = number

    @property
    def full_number(self) -> str:
        """Returns the full phone number as a string."""
        return f"+{self.country_code}{self.number}"

    def __str__(self) -> str:
        """Returns the string representation of the phone number."""
        return self.full_number

    def __repr__(self) -> str:
        """Returns the official string representation of the phone number."""
        return f"PhoneNumber(country_code={self.country_code}, number={self.number})"
