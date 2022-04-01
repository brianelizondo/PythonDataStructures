def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reverse_list = list(phrase)
    reverse_list.reverse()
    return "".join(reverse_list)
