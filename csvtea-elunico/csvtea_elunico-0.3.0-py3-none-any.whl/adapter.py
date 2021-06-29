import abc
from typing import TypeVar


class OutputAdapter(abc.ABC):
    """
    Output adapters take the output of CSVParser and adapt it to a particular format. They are NOT passed into the
    CSVParser but can be instantiated and used outside of the class. They should implement a `adapt` method that
    takes a single list[list[str]] as is returned from the `parse` method of CSVParser. It can return any type.
    """

    def __init__(self):
        pass

    T = TypeVar('T')

    @abc.abstractmethod
    def adapt(self, output: list[list[str]]) -> T:
        """
        takes a single list[list[str]] as is returned from the `parse` method of CSVParser. It can return any type.
        :param output: the output from the CSVParser to be adapted
        :return: The transformed data
        """
        pass


class DictOutputAdapter(OutputAdapter):
    """
    Transforms the CSV output into a list of dictionaries. Each dictionary in the list has the same keys which correspond
    to the values in the first row of the CSV (the header row) and whose keys are one of the entries in the CSV file
    """
    def adapt(self, output: list[list[str]]) -> list[dict[str, str]]:
        headers = output[0]
        entries = output[1:]
        result = []
        for entry in entries:
            result.append({k: v for k, v in zip(headers, entry)})
        return result
