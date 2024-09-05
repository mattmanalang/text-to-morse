"""Unit Testing for the Text-to-Morse program."""

import unittest
from text_to_morse import MorseCode

class TestMorseConverter(unittest.TestCase):
    """Test Case Class"""
    def test_canary(self):
        """Canary test to make sure everything is working."""
        self.assertTrue(True)

    def test_single_letter(self):
        """Translating a single letter."""
        morse = MorseCode()
        self.assertEqual(morse.to_morse('a'), '.-')
        self.assertEqual(morse.to_morse('b'), '-...')

# Only needed if you are going to be running the tests manually using this file.
if __name__ == "__main__":
    unittest.main()
