#pylint: skip-file
from rest_framework.permissions import BasePermission


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

def get_guest_permissions_class(allowed_actions=None):
    """
    get a guest permissions class with the given allowed actions
    :param allowed_actions: list of allowed actions
    :return: GuestPermissions class with the given allowed actions
    """

    if allowed_actions is None:
        allowed_actions = ['list', 'retrieve']

    class GuestPermissions(BasePermission):
        """
        Guest (AnonymousUser) Permissions class

        allows for providing a list of allowed view action that should be allow for this endpoint

        default allowed actions are [list, retrieve]
        """
        _allowed_actions = allowed_actions

        def has_permission(self, request, view):
            action = getattr(view, 'action', None)
            return request.user.is_anonymous() and action in self._allowed_actions

        def __repr__(self):
            "{0}: {1}".format(self.__class__.__name__, self._allowed_actions)

    return GuestPermissions