def summation(lower, upper):
    """Arguments: A lower bound and an upper bound
    Returns: the sum of the numbers from the lower through upper
    """

    result = 0
    while lower <= upper:
        result += lower
        lower += 1
    return result