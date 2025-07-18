
import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.transformers.data_transformer import transform_data

class TestDataTransformer(unittest.TestCase):

    def test_transform_data(self):
        articles = [
            {
                'title': 'Test Article',
                'url': 'http://example.com/article',
                'summary': 'This is a test summary.',
                'publication_date': '2024-01-01T00:00:00',
                'source': 'Test Source'
            }
        ]
        
        transformed_articles = transform_data(articles)
        
        self.assertEqual(len(transformed_articles), 1)
        self.assertIn('id', transformed_articles[0])
        self.assertEqual(transformed_articles[0]['title'], 'Test Article')

if __name__ == '__main__':
    unittest.main()
