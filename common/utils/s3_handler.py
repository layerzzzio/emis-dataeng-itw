import boto3
import json
import logging
from botocore.exceptions import ClientError
from datetime import datetime
import uuid


def upload_to_s3(bucket_name, filename, data):
    # Initialize a session using Amazon S3 credentials
    session = boto3.session.Session()
    s3 = session.resource('s3')

    # Convert Python dictionary to JSON string
    json_string = json.dumps(data)

    try:
        # Upload the JSON string as a file to the specified bucket
        s3.Bucket(bucket_name).put_object(Key=filename, Body=json_string)
        logging.info(f"File {filename} uploaded to {bucket_name}.")
    except ClientError as e:
        logging.error(f"Failed to upload {filename} to {bucket_name}: {e}")
        raise


def generate_s3_key(prefix: str, original_filename: str) -> str:
    # Use a timestamp and UUID to ensure uniqueness
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    unique_id = uuid.uuid4()
    # Construct the S3 key
    s3_key = f"{prefix}/{timestamp}-{unique_id}-{original_filename}"
    return s3_key

