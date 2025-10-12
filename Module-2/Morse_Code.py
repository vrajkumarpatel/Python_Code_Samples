morse_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--.."
}
text = input("Enter text (letters only): ").upper()
morse = ""
for letter in text:
    if letter in morse_dict:
        morse += morse_dict[letter] + " "
    else:
        morse += " "  # space for unknown characters
print("Morse code:", morse)
