import uuid

from datagen.src.errors.generator_errors import errors


def generate_uuid(version_uuid: int, name_space_dns: str = None) -> uuid.UUID:
    """
    Generates a UUID of the specified version.

    :param version_uuid: The version of the UUID to generate (1, 3, 4, or 5).
    :param name_space_dns: The DNS namespace for versions 3 and 5. Required for these versions.
    :return: A UUID object.
    :raises errors_for_utils_data.UuidError: If an invalid version is provided.
    :raises errors_for_utils_data.UuidNameSpaceDNSIsNotProvidedError: If name_space_dns is not provided for versions 3 or 5.
    """
    if version_uuid not in [1, 3, 4, 5]:
        raise errors.UuidError("Invalid UUID version. Please provide a version between 1 and 5.")

    if version_uuid == 1:
        return uuid.uuid1()

    if version_uuid in [3, 5]:
        if name_space_dns is None:
            raise errors.UuidNameSpaceDNSIsNotProvidedError(
                f"Namespace DNS is required for UUID version {version_uuid}."
            )
        namespace = uuid.NAMESPACE_DNS
        return uuid.uuid3(namespace, name_space_dns) if version_uuid == 3 else uuid.uuid5(namespace, name_space_dns)

    return uuid.uuid4()


# # Example usage
# try:
#     print(generate_uuid(1))
#     print(generate_uuid(3, "example.com"))
#     print(generate_uuid(4))
#     print(generate_uuid(5, "example.com"))
# except errors_for_utils_data.UuidError as e:
#     print(e)
# except errors_for_utils_data.UuidNameSpaceDNSIsNotProvidedError as e:
#     print(e)
