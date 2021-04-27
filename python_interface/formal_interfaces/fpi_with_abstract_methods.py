"""
Use abstract methods
"""

from abc import ABCMeta, abstractmethod


class FormalParserInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, "load_data_source")
            and callable(subclass.load_data_source)
            and hasattr(subclass, "extract_text")
            and callable(subclass.extract_text)
        )

    @abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError


class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF
    >>> pdf_pars = PdfParserNew()
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


class EmailParserNew(FormalParserInterface):
    """Extract text from an email
    >>> eml_pars = EmailParserNew()
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: Can't instantiate abstract class EmailParserNew with abstract methods extract_text
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmailParserNew.
        Doesn't override FormalParserInterface.extract_text()"""
        pass
