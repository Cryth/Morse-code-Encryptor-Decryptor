from resources import alphabet_morse, morse_alphabet_dec


def from_morse(input_message):
    decrypted_message = ""
    # split the input into list of words
    words = input_message.split("/")
    # decrypt every word
    for word in words:
        # split word into characters
        characters = word.split()
        # decrypt characters
        for char in characters:
            # append decrypted character
            decrypted_message += morse_alphabet_dec[char]
        # append whitespace after word
        decrypted_message += " "
    # returns the decrypted message
    return decrypted_message
    


def input_control(input_message):
    # every character in the input message is checked for validity
    for char in input_message:
        # if there is no such character in the alphabet -> returns false, encryption not possible
        if char not in alphabet_morse:
            return False
    return True
