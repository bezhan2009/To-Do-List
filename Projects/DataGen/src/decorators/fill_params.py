import inspect

from src.utils.random_data import random_data
from src.utils.url_generate import Url


def fill_randomly(func):
    def wrapper(*args):
        sig = inspect.signature(func)
        params = sig.parameters
        fillers = []
        for _, param in params.items():
            if not param.annotation:
                raise ValueError(f"Parameter {param.name} must have annotation.")
            annotation = param.annotation
            if annotation == str:
                fillers += [random_data(annotation, 10)]
            elif annotation == Url:
                fillers.append(random_data(annotation, 15))

            else:
                fillers.append(random_data(annotation))
        return func(*fillers)

    return wrapper
