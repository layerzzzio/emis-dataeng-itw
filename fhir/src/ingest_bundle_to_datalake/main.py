from typing import List
from common.etl.abstract_etl import AbstractETL


class IngestBundleToDatalake(AbstractETL):

    def __init__(self, s3_bkt: str):
        self.s3_bucket = s3_bkt

    def extract(self) -> List[dict]:
        # read data from S3
        return []

    def transform(self, extracted_data: List[dict]) -> List[dict]:
        # No transformation needed, just return the extracted data
        return extracted_data

    def load(self, extracted_data: List[dict]) -> None:
        # load data to datalake raw/fhir folder
        pass


if __name__ == "__main__":
    # Example usage
    s3_bucket = "your-s3-bucket-name"

    # Initialize the ETL process
    etl_process = IngestBundleToDatalake(s3_bucket)

    # Run the ETL process
    etl_process.run()
