# /tests/test_utils.py

import unittest
from scripts.utils import chunk_text

class TestUtils(unittest.TestCase):

    def test_chunk_text(self):
        text = "Word " * 50  # 50 words
        chunks = chunk_text(text, max_length=100)
        self.assertIsInstance(chunks, list)
        self.assertTrue(len(chunks) > 0)
        for chunk in chunks:
            self.assertTrue(len(chunk) <= 100)

if __name__ == '__main__':
    unittest.main()
