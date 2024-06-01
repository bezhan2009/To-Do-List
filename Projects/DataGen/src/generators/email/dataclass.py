class GeneratedEmail:
    """
    Represents a generated email address.

    Attributes:
        email (str): The generated email address.
    """

    def __init__(self, email: str) -> None:
        self.email: str = email

    def __str__(self) -> str:
        """Returns the string representation of the generated email."""
        return self.email

    def __repr__(self) -> str:
        """Returns the official string representation of the generated email."""
        return f"GeneratedEmail(email={self.email})"
