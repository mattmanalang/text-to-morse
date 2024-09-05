"""Unit Testing for the Text-to-Morse program."""

import unittest
from text_to_morse import MorseCode

class TestMorseConverter(unittest.TestCase):
    """Test Case Class"""
    def test_canary(self):
        """Canary test to make sure everything is working."""
        self.assertTrue(True)

    def test_single_character(self):
        """Translating a single letter."""
        morse = MorseCode()
        self.assertEqual(morse.to_morse('a'), '.-')
        self.assertEqual(morse.to_morse('3'), '...--')
        self.assertEqual(morse.to_morse('?'), '..--..')

    def test_n_characters(self):
        """Translating n-letters."""
        morse = MorseCode()
        self.assertEqual(morse.to_morse('ab'), '.- -...')
        self.assertEqual(morse.to_morse('c1'), '-.-. .----')
        self.assertEqual(morse.to_morse('e7='), '. --... -...-')

    def test_n_characters_with_spaces(self):
        """Translating n-letters with the addition of spaces. 
        Spaces should be represented by a forward slash (/)"""
        pass


# Only needed if you are going to be running the tests manually using this file.
if __name__ == "__main__":
    unittest.main()
