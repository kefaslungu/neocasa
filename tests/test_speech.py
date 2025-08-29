import unittest
from src.speech import voices, config

class TestVoices(unittest.TestCase):
    def test_us_voices_dict(self):
        self.assertIsInstance(voices.us_voices, dict)
        self.assertIn('Andrew (Male)', voices.us_voices)
        self.assertTrue(voices.us_voices['Andrew (Male)'].startswith('en-US'))

class TestConfig(unittest.TestCase):
    def test_config_values(self):
        self.assertTrue(hasattr(config, 'voice'))
        self.assertTrue(hasattr(config, 'bitrate'))
        self.assertIsInstance(config.voice, str)
        self.assertIsInstance(config.bitrate, str)

if __name__ == '__main__':
    unittest.main()
