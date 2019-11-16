from typing import Optional, TypeVar

T = TypeVar("T", int, float)


def limit(value: T, lower: Optional[T] = None, upper: Optional[T] = None) -> T:
    """
    Clamps :parameter:`value` to between `lower` and `upper`.

    :param value: The value to clamp.
    :param lower: The lower limit to clamp to.  Defaults to 0.
    :param upper: The upper limit to clamp to.  Defaults to 1.

    :returns: The clamped value

    >>> limit(10)
    1
    >>> limit(10.0)
    1.0
    >>> limit(-10)
    0
    >>> limit(-10.0)
    0.0
    >>> limit(0.5)
    0.5
    >>> limit(500, 0, 255)
    255
    >>> limit(500.0, 0, 255)
    255
    """
    if lower is None:
        lower = type(value)(0)
    if upper is None:
        upper = type(value)(1)
    return max(lower, min(value, upper))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
