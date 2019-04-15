from resources import alphabet, morse_alphabet


def to_morse(input_message):
    encrypted_message = ""

    # for cycle that iterates trough the message encrypting all the characters
    for char in input_message:
        # if there is empty space, "/" is appended to the encrypted message
        if char == " ":
            encrypted_message += "/"
        else:
            # gets the to-be encrypted character from the imported dictionary,
            # empty space is added so decryption is possible
            encrypted_char = morse_alphabet[char] + " "

            # encrypted character is appended to the encrypted message
            encrypted_message += encrypted_char
    # returns encrypted message
    return encrypted_message


def input_control(input_message):
    # every character in the input message is checked for validity
    for char in input_message:
        # if there is no such character in the alphabet -> returns false, encryption not possible
        if char not in alphabet:
            return False
    return True
