def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_swap = ""
    for char in phrase:
        char_lower = char.lower()
        if char_lower == to_swap.lower():
            phrase_swap += char.swapcase()
        else:
            phrase_swap += char

    return phrase_swap
