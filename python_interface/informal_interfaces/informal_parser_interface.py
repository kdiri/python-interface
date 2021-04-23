class InformalParserInterface:
    """
    Informal parser interface
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """
        Load from file to load the text
        :param path: file path
        :param file_name: file name
        :return: str
        """
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """
        Extract the text from the currently loaded file
        :param full_file_name:
        :return: dict
        """
        pass


class PdfParser(InformalParserInterface):
    """Extract the text from a pdf"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass


class EmailParser(InformalParserInterface):
    """Extract the text from a pdf"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_name: str) -> dict:
        """A method defined in only EmailParser.
        Doesn't overrides InformalParserInterface.extract_text()"""
        pass


"""
>>> # Check if both PdfParser and EmlParser implement InformalParserInterface
>>> issubclass(EmailParser, InformalParserInterface)
True
>>> issubclass(PdfParser, InformalParserInterface)
True
"""
