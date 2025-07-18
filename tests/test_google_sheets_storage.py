
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.storage.google_sheets_storage import save_to_google_sheets

class TestGoogleSheetsStorage(unittest.TestCase):

    @patch('src.storage.google_sheets_storage.get_google_sheets_client')
    def test_save_to_google_sheets(self, mock_get_google_sheets_client):
        # Create a mock sheet object
        mock_sheet = MagicMock()
        mock_sheet.row_count = 1  # Simulate a sheet with a header
        mock_sheet.find.return_value = None  # Simulate that the article is not in the sheet
        
        # Configure the mock client to return the mock sheet
        mock_get_google_sheets_client.return_value = mock_sheet
        
        articles = [
            {
                'id': 'test_id',
                'title': 'Test Article',
                'url': 'http://example.com/article',
                'summary': 'This is a test summary.',
                'publication_date': '2024-01-01T00:00:00',
                'source': 'Test Source',
                'collection_date': '2024-01-01T00:00:00',
                'tags': ''
            }
        ]
        
        save_to_google_sheets(articles)
        
        # Verify that the sheet.append_row method was called with the correct data
        mock_sheet.append_row.assert_called_once()
        # Can be more specific with:
        # self.assertEqual(mock_sheet.append_row.call_args[0][0], ['test_id', 'Test Article', ...])

if __name__ == '__main__':
    unittest.main()
