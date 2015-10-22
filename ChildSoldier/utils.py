#pylint: skip-file


def dict_from_attrs(obj, list_of_attrs):
    """
    :param obj: Object to have attributes extracted
    :param list_of_attrs: List of attributes to extract
    :return: Dictionary built by extracting the attributes from the given object
    """
    return {attr: getattr(obj, attr) for attr in list_of_attrs}


def dict_with_keys(dictionary, list_of_keys):
    """
    :param dictionary: Dict to have keys extracted
    :param list_of_keys: List of keys to extract
    :return: New dictionary using the given dict, containing only the given keys
    """
    return {key: dictionary[key] for key in list_of_keys}
