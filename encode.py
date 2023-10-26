# Efua Emuan
def encode(password):
    encoded_password = ""
    for digit in password:
        if digit.isdigit():
            # Shift each digit up by 3
            encoded_digit = str((int(digit) + 3) % 10)
            encoded_password += encoded_digit
        else:
            # If the character is not a digit, keep it unchanged
            encoded_password += digit
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        if digit.isdigit():
            # Shift each digit back down by 3
            decoded_digit = str((int(digit) - 3) % 10)
            decoded_password += decoded_digit
        else:
            # If the character is not a digit, keep it unchanged
            decoded_password += digit
    return decoded_password

def main():
    stored_password = None  # Initialize with no stored password

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            stored_password = encoded_password
            print("Your password has been encoded and stored!")

        elif choice == "2":
            if stored_password is not None:
                decoded_password = decode(stored_password)
                print(f"The encoded password is: {stored_password}, and the original password is {decoded_password}")
            else:
                print("No password has been stored yet.")

        elif choice == "3":
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
