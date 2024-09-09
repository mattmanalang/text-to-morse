"""Driver program for the text-to-morse project."""

from text_to_morse import MorseCode

morse = MorseCode()

print("Allowed characters: Letters (A-Z), Numbers (0-9), Punctuation (. , ? / ( ) : = + - \' \" @)")
user_msg = input("Enter message to be converted into Morse: ")
morse_code = morse.to_morse(user_msg)

morse.write_to_file(morse_code)
