from typing import List
from common.etl.abstract_etl import AbstractETL
import json

from common.utils.s3_handler import upload_to_s3, generate_s3_key
from fhir.src.ingest_bundle_to_landing.extract import fetch_fhir_bulk


class IngestBundleToLanding(AbstractETL):

    def __init__(self, api_url: str, s3_bkt: str):
        self.source_api_url = api_url
        self.s3_bucket = s3_bkt

    def extract(self) -> List[dict]:
        json_files = fetch_fhir_bulk(self.source_api_url)
        return json_files

    def transform(self, extracted_data: List[dict]) -> List[dict]:
        # No transformation needed, just return the extracted data
        return extracted_data

    def load(self, extracted_data: List[dict]) -> None:
        # Logic to load to S3, assuming extracted_data is a list of JSON objects
        for index, record in enumerate(extracted_data):
            json_data = json.dumps(record)
            # Generate a unique S3 key for each record, including the index
            s3_key = generate_s3_key('to_processed', f'patient_{index}.json')
            upload_to_s3(self.s3_bucket, s3_key, json_data)


if __name__ == "__main__":
    # Example usage
    source_api_url = "http://api.fhir.org/v1/bundles"
    s3_bucket = "your-s3-bucket-name"

    # Initialize the ETL process
    etl_process = IngestBundleToLanding(source_api_url, s3_bucket)

    # Run the ETL process
    etl_process.run()
