
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.collectors.rss_collector import collect_rss_feeds

class TestRssCollector(unittest.TestCase):

    @patch('src.collectors.rss_collector.feedparser')
    def test_collect_rss_feeds(self, mock_feedparser):
        # Create a mock feed object
        mock_feed = MagicMock()
        mock_feed.bozo = 0
        mock_feed.feed.title = 'Test Feed'
        mock_feed.entries = [
            {
                'title': 'Test Article',
                'link': 'http://example.com/article',
                'summary': 'This is a test summary.',
                'published': '2024-01-01T00:00:00'
            }
        ]
        
        # Configure the mock feedparser to return the mock feed
        mock_feedparser.parse.return_value = mock_feed
        
        # Set the RSS_FEEDS configuration for the test
        with patch('src.collectors.rss_collector.Config') as mock_config:
            mock_config.RSS_FEEDS = ['http://example.com/feed']
            
            articles = collect_rss_feeds()
            
            self.assertEqual(len(articles), 1)
            self.assertEqual(articles[0]['title'], 'Test Article')

if __name__ == '__main__':
    unittest.main()
