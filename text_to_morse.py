"""Main file for the text-to-morse code program"""
import datetime as dt

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
            if character == ' ':
                ciphertext += "/ "  # Spaces are visually represented here by a forward slash (/)
            elif not MorseCode.MORSE_CHART.get(character.upper()):
                ciphertext += "# "
            else:
                ciphertext += f"{MorseCode.MORSE_CHART.get(character.upper())} "

        return ciphertext.strip()
    
    def write_to_file(self, text):
        """Writes string content to a file with the current time stamp as 'YYYY-MM-DD HH_MM UTC' as the file name."""
        current_time_utc = dt.datetime.now(tz=dt.timezone.utc)
        filename = f"{current_time_utc.year}-{current_time_utc.month}-{current_time_utc.day} "\
            f"{current_time_utc.hour}_{current_time_utc.minute} UTC"
        with open(f"{filename}.txt", "w", encoding="utf-8") as output:
            output.write(text)


morse = MorseCode()

print("Allowed characters: Letters (A-Z), Numbers (0-9), Punctuation (. , ? / ( ) : = + - \' \" @)")
user_msg = input("Enter message to be converted into Morse: ")
ciphertext = morse.to_morse(user_msg)

morse.write_to_file(ciphertext)
