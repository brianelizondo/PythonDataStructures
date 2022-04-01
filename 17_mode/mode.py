def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    basic_values = set(nums)
    max_value = 0
    for num in basic_values:
        if nums.count(num) > max_value:
            max_value = nums.count(num)
            max_number = num

    return max_number