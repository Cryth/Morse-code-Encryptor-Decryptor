from morse_encryption import to_morse, input_control


def main():
    while True:
        try:
            message = input("Enter a message to encrypt: ").upper()  # gets input from user
            if message == "X1X1":  # typing this string stops the cycle
                break
            else:
                if not input_control(message):  # inputs gets checked for invalid characters
                    raise TypeError  # if there's an invalid char -> raise TypeError
                print(to_morse(message))  # prints the encrypted message
        except TypeError:
            print("Invalid input! Fix the message.")


if __name__ == '__main__':
    main()
