from abc import ABC, abstractmethod
from pyspark.sql import DataFrame


class AbstractETL(ABC):
    @abstractmethod
    def extract(self):
        """Extract data from the data source."""
        pass

    @abstractmethod
    def load(self, extracted_data):
        """Load the extracted data into the target destination."""
        pass

    @abstractmethod
    def transform(self, loaded_data) -> DataFrame:
        """Transform the data after loading."""
        pass
