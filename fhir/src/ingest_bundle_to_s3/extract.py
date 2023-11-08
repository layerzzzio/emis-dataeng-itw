# extract.py
from common.utils.api_client import make_request, ReqType


def fetch_fhir_bulk(base_url: str):
    # Assuming the FHIR data can be accessed via a GET request to the base_url
    try:
        fhir_data = make_request(ReqType.GET, base_url, {})
        return fhir_data
    except Exception as e:
        # Handle any exceptions accordingly
        # Depending on your use case, you may want to log the error, retry the request, etc.
        raise e