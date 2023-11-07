from common.etl.abstract_etl import ETLProcess
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col
import json

from fhir.src.fetch_patient_bundle.extract import fetch_fhir_bulk


class JSONToTabular(ETLProcess):

    def __init__(self, api_url: str, dest_path: str):
        self.source_api_url = api_url
        self.destination_path = dest_path
        self.spark = SparkSession.builder.appName("JSONToTabular").getOrCreate()

    def extract(self) -> DataFrame:
        fetch_fhir_bulk('http://api.fhir.org//v1/resources')
        # Here you would use requests or another method to fetch your JSON data
        # For this example, let's assume you have the JSON data already loaded
        json_data = [{"id": 1, "value": "A"}, {"id": 2, "value": "B"}]  # This would be replaced with your actual data fetching logic
        rdd = self.spark.sparkContext.parallelize([json.dumps(record) for record in json_data])
        df = self.spark.read.json(rdd)
        return df

    def transform(self, df: DataFrame) -> DataFrame:
        # Perform transformations on the DataFrame
        # For example, selecting columns or converting data types
        transformed_df = df.select(
            col("id").cast("integer"),
            col("value").cast("string")
        )
        return transformed_df

    def load(self, df: DataFrame):
        # Load the transformed DataFrame to the destination
        df.write.format("parquet").save(self.destination_path)

    def run(self):
        # The run method orchestrates the ETL process
        extracted_df = self.extract()
        transformed_df = self.transform(extracted_df)
        self.load(transformed_df)


if __name__ == "__main__":
    # Example usage
    source_api_url = "http://api.fhir.org/v1/resources"
    destination_path = "/path/to/store/tabular/data"

    # Initialize the ETL process
    etl_process = JSONToTabular(source_api_url, destination_path)

    # Run the ETL process
    etl_process.run()
