"""Unit Testing for the Text-to-Morse program."""

import unittest
from io import TextIOWrapper

from text_to_morse import MorseCode

class TestMorseConverter(unittest.TestCase):
    """Test Case Class"""
    def test_canary(self):
        """Canary test to make sure everything is working."""
        self.assertTrue(1+1, 2)

    def test_single_character(self):
        """Translating a single letter."""
        morse = MorseCode()
        self.assertEqual(morse.to_morse('a'), '.-')
        self.assertEqual(morse.to_morse('3'), '...--')
        self.assertEqual(morse.to_morse('?'), '..--..')

    def test_n_characters(self):
        """Translating n-letters. Each letter is separated by a pause that is equal to a dit."""
        morse = MorseCode()
        self.assertEqual(morse.to_morse('ab'), '.- -...')
        self.assertEqual(morse.to_morse('c1'), '-.-. .----')
        self.assertEqual(morse.to_morse('e7='), '. --... -...-')

    def test_n_characters_with_spaces(self):
        """Translating n-letters with the addition of spaces between words. 
        Spaces are audibly represented by 7 empty dits, but here we are visually using '/'."""
        morse = MorseCode()
        self.assertEqual(morse.to_morse("a b"), ".- / -...")
        self.assertEqual(morse.to_morse("hi there"), ".... .. / - .... . .-. .")

    def test_undefined_characters(self):
        """Translating multiple words with the inclusion of characters not defined in Morse Code.
        Undefined characters will be visually represented here using '#'."""
        morse = MorseCode()
        # The exclamation point is not defined in Morse.
        self.assertEqual(morse.to_morse("hello world!"),
                         ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. #")
        self.assertEqual(morse.to_morse("!#$%^& ***"), "# # # # # # / # # #")

    def test_file_writer(self):
        """Testing for successful file creation."""
        morse = MorseCode()
        self.assertIsInstance(morse.write_to_file("test"), TextIOWrapper)


# Only needed if you are going to be running the tests manually using this file.
if __name__ == "__main__":
    unittest.main()
