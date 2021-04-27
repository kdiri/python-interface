class PersonMeta(type):
    """A Person metaclass"""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, "name")
            and callable(subclass.name)
            and hasattr(subclass, "age")
            and callable(subclass.age)
        )


class PersonSuper:
    """A Person superclass"""

    def name(self) -> str:
        pass

    def age(self) -> int:
        pass


class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""

    pass


# Inheriting subclasses
class Employee(PersonSuper):
    """
    Inherits from PersonSuper.
    PersonSuper will appear in Employee.__mro__
    >>> Employee.__mro__
    >>> (<class '__main__.Employee'>, <class '__main__.PersonSuper'>, <class 'object'>)
    """

    pass


class Friend:
    """Built implicitly from Person.
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person is not Friend.__mro__
    >>> Friend.__mro__
    >>> (<class '__main__.Friend'>, <class 'object'>)
    """

    def name(self):
        pass

    def age(self):
        pass
