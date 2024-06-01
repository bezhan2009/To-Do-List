class RandomElements:
    """
    Represents a collection of randomly selected elements.

    Attributes:
        elements (list): The list of selected elements.
    """

    def __init__(self, elements: list) -> None:
        self.elements: list = elements

    def __str__(self) -> str:
        """Returns the string representation of the random elements."""
        return str(self.elements)

    def __repr__(self) -> str:
        """Returns the official string representation of the random elements."""
        return f"RandomElements(elements={self.elements})"
