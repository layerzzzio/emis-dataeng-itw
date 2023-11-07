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
    def transform(self, extracted_data) -> DataFrame:
        """Transform the extracted data after extraction."""
        pass

    def run(self):
        extracted_data = self.extract()
        transformed_data = self.transform(extracted_data)
        self.load(transformed_data)
