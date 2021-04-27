"""
Using Subclass Detection With Registration
"""

import abc


class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "load_data_source")
            and callable(subclass.load_data_source)
            and hasattr(subclass, "extract_text")
            and callable(subclass.extract_text)
            or NotImplemented
        )


class PdfParserNew:
    """Extract text from a PDF
    >>> issubclass(PdfParserNew, FormalParserInterface)
    >>> True
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


@FormalParserInterface.register
class EmailParserNew:
    """Extract the text from a email
    >>> issubclass(EmailParserNew, FormalParserInterface)
    >>> True
    # Because extract text wasn't defined in EmailParserNew
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_name: str) -> dict:
        """A method defined in only EmailParser.
        Doesn't overrides UpdatedInformalParserInterface.extract_text()
        """
        pass
