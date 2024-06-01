from src.errors.generator_errors import errors


def type_get(type_element):
    """
    Returns the corresponding Python type for the given string representation.

    Args:
        type_element (str): The string representation of the data type.
                            Accepted values are 'int', 'float', 'str', 'bool',
                            'list', 'dict', 'tuple', and 'set'.

    Returns:
        type: The corresponding Python type if the type_element is recognized.
              For example, if type_element is 'int', the function returns the int type.

    Raises:
        errors.TypeGetError: If the type_element is not recognized.
                             The function raises a custom error indicating
                             that the data type is unknown.
    """
    if type_element == 'int':
        return int
    elif type_element == 'float':
        return float
    elif type_element == 'str':
        return str
    elif type_element == 'bool':
        return bool
    elif type_element == 'list':
        return list
    elif type_element == 'dict':
        return dict
    elif type_element == 'tuple':
        return tuple
    elif type_element == 'set':
        return set
    else:
        return errors.TypeGetError("Unknown data type")
