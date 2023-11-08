# File: tests/test_extract.py
import unittest
from unittest.mock import patch

from common.utils.api_client import ReqType
from fhir.src.ingest_bundle_to_landing.extract import fetch_fhir_bulk


class TestExtract(unittest.TestCase):

    @patch('fhir.src.ingest_bundle_to_landing.extract.make_request')
    def test_fetch_fhir_bulk(self, mock_make_request):
        # Setup the mock response
        mock_response = {'data': 'expected response'}
        mock_make_request.return_value = mock_response

        # Call the function
        result = fetch_fhir_bulk('http://dummy_url')

        # Assertions to ensure the function behaves as expected
        self.assertEqual(result, mock_response)
        mock_make_request.assert_called_with(ReqType.GET, 'http://dummy_url', {})


if __name__ == '__main__':
    unittest.main()
