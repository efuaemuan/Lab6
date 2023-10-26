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


if __name__ == "__main__":
    password = input("Please enter your password to encode: ")
    encoded_password = encode(password)
    print(f"Your password has been encoded and stored! {encoded_password}")
