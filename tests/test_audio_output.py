# /tests/test_audio_output.py

import unittest
from scripts.audio_output import play_audio
from unittest.mock import patch

class TestAudioOutput(unittest.TestCase):

    @patch('scripts.audio_output.pygame.mixer.music')
    def test_play_audio(self, mock_music):
        # Mock the pygame.mixer.music methods
        mock_music.load.return_value = None
        mock_music.play.return_value = None
        mock_music.get_busy.side_effect = [True, False]

        play_audio("audio/test_output.wav")
        mock_music.load.assert_called_once_with("audio/test_output.wav")
        mock_music.play.assert_called_once()
        self.assertEqual(mock_music.get_busy.call_count, 2)

if __name__ == '__main__':
    unittest.main()
