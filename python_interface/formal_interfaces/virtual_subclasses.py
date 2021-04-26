import abc


class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass


Double.register(float)


@Double.register
class Double64:
    """A 64-bit double-precision floating-point number
    >>> issubclass(Double64, Double)
    >>> True
    """
    pass
