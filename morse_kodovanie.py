from morse_encryption import to_morse, input_control


def main():
    while True:
        try:
            message = input("Zadajte text pre šifrovanie: ").upper()
            if message == "X1X1":  # ukoncenie programu
                break
            else:
                if not input_control(message):  # skontrolovanie inputu
                    raise TypeError  # ak sprava obsahuje zle znaky raisne sa TypeError (exception)
                print(to_morse(message))  # vypisanie sifrovaneho textu
        except TypeError:
            print("Vyskytla sa chyba, skontrolujte input!")


if __name__ == '__main__':
    main()
