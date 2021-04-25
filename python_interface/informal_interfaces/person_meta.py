
class PersonMeta(type):
    """A Person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, "name") and
            callable(subclass.name) and
            hasattr(subclass, "age") and
            callable(subclass.age)
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
