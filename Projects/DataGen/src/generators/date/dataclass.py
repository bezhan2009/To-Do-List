from datetime import datetime


class GeneratedDate:
    """
    Represents a generated date and optional time.

    Attributes:
        date (datetime): The generated date and time.
    """

    def __init__(self, date: datetime) -> None:
        self.date: datetime = date

    def __str__(self) -> str:
        """Returns the string representation of the generated date."""
        return self.date.isoformat()

    def __repr__(self) -> str:
        """Returns the official string representation of the generated date."""
        return f"GeneratedDate(date={self.date})"
