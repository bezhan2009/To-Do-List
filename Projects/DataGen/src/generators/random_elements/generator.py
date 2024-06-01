import random

try:
    from .dataclass import RandomElements
except ImportError:
    from dataclass import RandomElements


def generate_random_elements(input_list: list, num_elements: int) -> RandomElements:
    """
    Generates random elements from the given list.

    :param input_list: List from which to choose random elements.
    :param num_elements: Number of random elements to select.
    :return: A RandomElements object with the selected elements.
    :raises ValueError: If num_elements is greater than the length of input_list.
    """
    if num_elements > len(input_list):
        raise ValueError("Number of random elements cannot exceed the size of the input list.")

    selected_elements = random.sample(input_list, num_elements)
    return RandomElements(selected_elements)
