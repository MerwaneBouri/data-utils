import math


def is_fibonacci_number(number):
    """Checks if the given number is a fibonacci number

    Parameters
    ----------
    number: int
        The number to test

    Returns
    -------
    bool
        True if number is a Fibonacci number
    """
    return (
        math.sqrt(5 * number**2 + 4).is_integer()
        or math.sqrt(5 * number**2 - 4).is_integer()
    )
