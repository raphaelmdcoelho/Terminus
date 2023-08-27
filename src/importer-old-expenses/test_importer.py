# test_importer.py

import unittest
from unittest.mock import patch, Mock
import importer


@patch('importer.SPREADSHEET_ID', 'dummy_spreadsheet_id')
@patch('importer.GOOGLE_CREDENTIALS', {'dummy': 'credentials'})
class TestImporter(unittest.TestCase):

    @patch('importer.build')
    @patch('importer.Credentials.from_service_account_info')
    def test_initialize_api_client(self, MockCredentials, MockBuild):
        MockCredentials.return_value = Mock()
        MockBuild.return_value = Mock()
        service = importer.initialize_api_client()
        self.assertIsNotNone(service)

    @patch('importer.build')
    def test_get_spreadsheet_data(self, MockBuild):
        mock_service = Mock()
        mock_sheet = Mock()
        mock_service.spreadsheets.return_value = mock_sheet
        mock_sheet.values().get().execute.return_value = {'values': [['data']]}
        MockBuild.return_value = mock_service

        values = importer.get_spreadsheet_data(mock_service)
        self.assertEqual(values, [['data']])


if __name__ == '__main__':
    unittest.main()
