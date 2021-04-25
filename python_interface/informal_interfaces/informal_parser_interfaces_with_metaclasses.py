class ParserMeta(type):
    """A parser metaclass that will be used for parser class creation"""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, "load_data_source")
            and callable(subclass.load_data_source)
            and hasattr(subclass, "extract_text")
            and callable(subclass.extract_text)
        )


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """
    This interface is used for concrete classes to inherit from.
    There is no need to define ParserMeta method any class as they are
    implicitly available via .__subclasscheck__().
    """
    pass


class PdfParserNew(UpdatedInformalParserInterface):
    """Extract the text from a pdf"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass


class EmailParserNew(UpdatedInformalParserInterface):
    """Extract the text from a pdf"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_name: str) -> dict:
        """A method defined in only EmailParser.
        Doesn't overrides UpdatedInformalParserInterface.extract_text()"""
        pass


"""
Here, you have a metaclass that’s used to create UpdatedInformalParserInterface. 
By using a metaclass, you don’t need to explicitly define the subclasses. 
Instead, the subclass must define the required methods. 
If it doesn’t, then issubclass(EmlParserNew, UpdatedInformalParserInterface) will return False.

>>> issubclass(PdfParserNew, UpdatedInformalParserInterface)
True
# UpdatedInformalParserInterface is a virtual base class of PdfParserNew
>>> issubclass(EmailParserNew, UpdatedInformalParserInterface)
False
# Because extract text wasn't defined in EmailParserNew
"""
