from common.utils.s3_handler import upload_to_s3

def load(json_data_list, bucket_name):
    for json_data in json_data_list:
        # You would create a unique filename for each JSON object
        filename = f"{json_data['id']}.json"  # Assuming each JSON object has a unique 'id' field
        upload_to_s3(bucket_name, filename, json_data)