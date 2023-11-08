from typing import Dict

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import explode
from delta.tables import DeltaTable

from common.etl.abstract_etl import AbstractETL
from fhir.src.transform_bundle_json_to_tabular.transform import process_resource_type


class TransformBundleJsonToTabular(AbstractETL):

    def __init__(self, dest_path: str):
        self.destination_path = dest_path
        self.spark = SparkSession.builder.appName("TransformBundleJsonToTabular").getOrCreate()

    def extract(self) -> None:
        pass

    def transform(self, df: DataFrame) -> Dict[str, DataFrame]:
        df = self.spark.read.json("/path/to/ddMMYYY/fhir_data.json")
        entries = df.select(explode("entry").alias("entry"))
        df_diagnostic_reports = process_resource_type(entries, 'diagnostic_reports', {})
        return {'diagnostic_reports': df_diagnostic_reports}

    def load(self, data: dict):
        # Assuming 'data' contains the dataframes to be written to Delta tables
        for table_name, df in data.items():
            # The full path to the Delta table
            delta_table_path = f"{self.destination_path}/{table_name}"

            # Check if the Delta table exists
            if DeltaTable.isDeltaTable(self.spark, delta_table_path):
                # Load the Delta table as a DeltaTable object
                delta_table = DeltaTable.forPath(self.spark, delta_table_path)

                # Perform the upsert (merge) operation
                delta_table.alias("target").merge(
                    df.alias("source"),
                    "target.primaryKey = source.primaryKey"
                ).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
            else:
                # If the table doesn't exist, write the DataFrame as a new Delta table
                df.write.format("delta").save(delta_table_path)


if __name__ == "__main__":
    # Initialize the ETL process
    etl_process = TransformBundleJsonToTabular(dest_path='to-be-defined')

    # Run the ETL process
    etl_process.run()
