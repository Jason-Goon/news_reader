# /tests/test_content_aggregator.py

import unittest
from scripts.content_aggregator import fetch_news, summarize_text
from unittest.mock import patch

class TestContentAggregator(unittest.TestCase):

    @patch('scripts.content_aggregator.requests.get')
    def test_fetch_news(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = '''
            <rss>
                <channel>
                    <item>
                        <title>Test News Title</title>
                        <description>Test news description content.</description>
                    </item>
                </channel>
            </rss>
        '''
        news_summary = fetch_news()
        self.assertIsInstance(news_summary, str)
        self.assertTrue(len(news_summary) > 0)

    def test_summarize_text(self):
        text = "Sentence one. Sentence two. Sentence three. Sentence four."
        summary = summarize_text(text)
        self.assertEqual(summary, "Sentence one. Sentence two.")

if __name__ == '__main__':
    unittest.main()
