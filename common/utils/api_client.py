import requests
import logging
from enum import Enum
from time import sleep


class ReqType(Enum):
    GET = 'get'
    POST = 'post'


def make_request(req_type: ReqType, url: str, data: dict, retries=3, backoff_factor=0.3):
    """Makes a GET or POST request with retry logic.

    Args:
        req_type (ReqType): The type of request, GET or POST.
        url (str): The URL to which the request is sent.
        data (dict): The data to send in the case of a POST request.
        retries (int): Number of retries if the request fails.
        backoff_factor (float): Factor to determine the delay between retries.

    Returns:
        dict: The JSON response from the API.

    Raises:
        ValueError: If the request method is not supported or the API returns an error.
        SystemExit: If the request fails after the specified number of retries.
    """
    for attempt in range(retries):
        try:
            if req_type == ReqType.GET:
                response = requests.get(url)
            elif req_type == ReqType.POST:
                response = requests.post(url, json=data)
            else:
                logging.error(f"Unsupported request operation: {req_type.value}")
                raise ValueError(f"Unsupported request operation: {req_type.value}")

            response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
            return response.json()  # If successful, return the JSON response

        except requests.exceptions.HTTPError as errh:
            logging.error(f"Http Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            logging.error(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            logging.error(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            logging.error(f"Error: {err}")

        if attempt < retries - 1:
            sleep(backoff_factor * (2 ** attempt))  # Exponential backoff

    raise SystemExit("Max retries exceeded")  # If the request failed all the attempts

# The make_request function should be located in a common library module (e.g., lib/api_client.py)
# because it's a generic function that can be reused across different parts of the project.
