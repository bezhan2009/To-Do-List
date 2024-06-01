from src.errors.generator_errors import errors


def length_validator(len_data):
    """
    Validation of data len
    :param len_data:
    :return: error or len_data
    """

    if len_data is None:
        raise errors_for_utils_data.LenNotProvidedError("Data length is not provided")
    if len_data < 0:
        raise errors_for_utils_data.LenGetError("Length cannot be negative")
    if len_data == 0:
        raise errors_for_utils_data.LenGetError("Length cannot be 0")
    if len_data >= 1:
        return
    if len_data >= 999:
        raise errors_for_utils_data.LenGetError("Length cannot be greater than 999")
