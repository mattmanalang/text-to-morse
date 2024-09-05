"""Main file for the text-to-morse code program"""

class MorseCode:
    """Used for converting text including letters, numbers, and punctuation, into morse code"""
    MORSE_CHART = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----',
        '.': '.-.-.-', ',': '--..--', '?': '..--..',
        '\'': '.----.', '/': '-..-.', '(': '-.--.',
        ')': '-.--.-', ':': '---...', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '"': '.-..-.',
        '@': '.--.-.'
    }

    def __init__(self) -> None:
        pass

    def to_morse(self, plaintext):
        """Takes input of a string and returns the morse code equivalent."""
        ciphertext = ""
        for character in plaintext:
            ciphertext += MorseCode.MORSE_CHART.get(character.upper())

        return ciphertext


morse = MorseCode()
