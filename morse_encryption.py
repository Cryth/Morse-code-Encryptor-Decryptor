from resources import *


def to_morse(input_message):
    encrypted_message = ""

    # for cyklus ktory prejde po celom slove a zasifruje kazdy znak
    for char in input_message:
        # ak je znak medzera zapise sa lomitko
        if char == " ":
            encrypted_message += "/"
        else:
            # ziska pismeno z abecedy a hned aj prideli medzeru aby bola mozna desifracia
            encrypted_char = morse_alphabet[char] + " "

            # do vysledneho stringu sa pripise sifrovane pismeno/cislo zo spravy
            encrypted_message += encrypted_char
    # vrati sifrovany text
    return encrypted_message


def input_control(input_message):
    # pre kazdy znak v inpute zisti ci je povoleny (podla zadanej abecedy vyssie)
    for char in input_message:
        # ak sa znak nenachadza v alphabet, vrati sa false
        if char not in alphabet:
            return False
    return True
