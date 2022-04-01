from unittest import result


def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    result = True
    for value in lst:
        if not isinstance(value, list):
            result = False

    return result