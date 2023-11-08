from pyspark.sql.functions import col


# Ex:
# diagnostic_report_fields = [
#     {"name": "id", "alias": "id"},
#     # Add more fields as required
# ]

def process_resource_type(entries_df, resource_type, fields):
    return (
        entries_df
        .where(col("entry.resource.resourceType") == resource_type)
        .select(*[col(f"entry.resource.{field['name']}").alias(field['alias']) for field in fields])
    )
