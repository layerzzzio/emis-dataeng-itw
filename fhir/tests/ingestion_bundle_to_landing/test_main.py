import unittest
from unittest.mock import patch

from common.utils.api_client import ReqType
from fhir.src.ingest_bundle_to_landing.main import IngestBundleToLanding


class TestETLProcess(unittest.TestCase):

    def setUp(self):
        # Setup code, if needed
        self.etl = IngestBundleToLanding('http://api.fhir.org/v1/bundles', 'your-s3-bucket')

    @unittest.mock.patch('fhir.src.ingest_bundle_to_landing.ingest_bundle_to_landing.make_request')
    def test_extract(self, mock_make_request):
        # Define the mock response
        mock_response = [{'patient_id': 1, 'data': '...'}, {'patient_id': 2, 'data': '...'}]
        mock_make_request.return_value = mock_response

        # Instantiate the ETL object within the test method to ensure patching applies
        etl = IngestBundleToLanding('http://api.fhir.org/v1/bundles', 'dummy_bucket')

        # Call the extract method
        result = etl.extract()

        # Assert the result
        self.assertEqual(result, mock_response)
        mock_make_request.assert_called_once_with(ReqType.GET, 'http://api.fhir.org/v1/bundles', {})

    def test_transform(self):
        # Mock input data
        input_data = [{'patient_id': 1, 'data': '...'}, {'patient_id': 2, 'data': '...'}]

        # Call the transform method
        result = self.etl.transform(input_data)

        # Assert the expected result
        self.assertEqual(result, input_data)  # Assuming transform does nothing in this case

    @patch('common.utils.s3_handler.upload_to_s3')
    def test_load(self, mock_upload_to_s3):
        # Mock input data
        input_data = [{'patient_id': 1, 'data': '...'}, {'patient_id': 2, 'data': '...'}]

        # Call the load method
        self.etl.load(input_data)

        # Assert the upload_to_s3 is called the right number of times
        self.assertEqual(mock_upload_to_s3.call_count, len(input_data))

        # Further tests can check if it's called with the right arguments


if __name__ == '__main__':
    unittest.main()
