import morse_decryption as md
import morse_encryption as me


def main():
    while True:
        try:
            # option block
            option = input("Do you want to Encrypt(E) or Decrypt(D)? ").upper()
            if option == "X1X1":  # typing this string stops the cycle
                break

            # encryption block
            elif option == "E": 
                message = input("Enter a message to encrypt: ").upper()
                if not me.input_control(message):
                    raise TypeError
                else:
                    print(me.to_morse(message))
            # decryption block
            elif option == "D":
                message = input("Enter a message to decrypt: ").upper()
                if not md.input_control(message):
                    raise TypeError
                else:
                    print(md.from_morse(message))
        # error handling
        except TypeError:
            print("Invalid input! Fix the message.")


if __name__ == '__main__':
    print("Starting application..")
    main()
    print("Application terminated.")