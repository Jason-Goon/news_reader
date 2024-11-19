# /tests/test_tts_processor.py

import unittest
import os
from scripts.tts_processor import generate_tts

class TestTTSProcessor(unittest.TestCase):

    def test_generate_tts(self):
        text = "This is a test for TTS generation."
        output_file = "audio/test_output.wav"

        if not os.path.exists('audio'):
            os.makedirs('audio')

        generate_tts(text, output_file)
        self.assertTrue(os.path.isfile(output_file))
        self.assertTrue(os.path.getsize(output_file) > 0)

        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
