import string


def encrypt(key, message, case_sensitive=False, numbers=False, symbols=False, show_warnings=False):
    """
        Returns the encrypted message using the caesar cipher.

        Parameters
        ----------
        key: int
            Number of positions the alphabet is shifted.

        message: str
            The message to be encrypted.

        case_sensitive: bool, default=False
            If False, the message will be converted to uppercase and
            the alphabet will only be uppercase. If True, the message 
            will be kept as it is and the alphabet will contain lowercase
            and uppercase letters.

        numbers: bool, default=False
            If True, the alphabet will include numbers. If False, the 
            alphabet will not include them.

        symbols: bool, default=False
            If True, the alphabet will include symbols. If False, the
            alphabet will not include them.

        show_warnings: bool. default=False
            If True, a warnings will be printed regarding your choice of
            characters in case the message contains any character not in
            the chosen alphabet.
    """
    # Case sensitive options
    if case_sensitive:
        # Use upper and lowercase characters
        alphabet = string.ascii_letters

    else:
        # Change the message and use only uppercase letters
        message = message.upper()
        alphabet = string.ascii_uppercase

    # Additional characters options
    if numbers:
        # Add all numbers
        alphabet += string.digits

    if symbols:
        # Add all symbols
        alphabet += string.punctuation

    # Make sure the key doesn't go beyond the alphabet's limits
    if key > len(alphabet):
        print("Key goes beyond the length of the alphabet.")
        return

    # Encrypt the message
    encrypted_message = ''

    for char in message:
        # Check for whitespace
        if char.isspace():
            encrypted_message += char

        elif char not in alphabet:
            encrypted_message += char

            if show_warnings:
                print(f'Character {char} is not in the defined alphabet.\n'
                      f'Argument numbers is {numbers}.\n'
                      f'Argument symbols is {symbols}.')

        else:
            # Get the character index
            char_idx = alphabet.index(char)

            # Get the new index after shifting
            new_idx = (char_idx - key) % 26

            # Use the new character in the encrypted message
            encrypted_message += alphabet[new_idx]

    return ''.join(encrypted_message)
    


def decrypt(key, message, case_sensitive=False, numbers=False, symbols=False):
    """
        Returns the decrypted message for the caesar cipher using the key.

        Parameters
        ----------
        key: int
            Number of positions the alphabet is shifted.

        message: str
            The message to be decrypted.

        case_sensitive: bool, default=False
            If False, the message will be converted to uppercase and
            the alphabet will only be uppercase. If True, the message 
            will be kept as it is and the alphabet will contain lowercase
            and uppercase letters.

        numbers: bool, default=False
            If True, the alphabet will include numbers. If False, the 
            alphabet will not include them.

        symbols: bool, default=False
            If True, the alphabet will include symbols. If False, the
            alphabet will not include them.
    """

    # Case sensitive options
    if case_sensitive:
        # Use upper and lowercase characters
        alphabet = string.ascii_letters

    else:
        # Change the message and use only uppercase letters
        message = message.upper()
        alphabet = string.ascii_uppercase

    # Additional characters options
    if numbers:
        # Add all numbers
        alphabet += string.digits

    if symbols:
        # Add all symbols
        alphabet += string.punctuation

    # Make sure the key doesn't go beyond the alphabet's limits
    if key > len(alphabet):
        print("Key goes beyond the length of the alphabet.")
        return

    # Decrypt the message
    decrypted_message = ''

    for char in message:
        # Check for whitespace
        if char.isspace():
            decrypted_message += char

        elif char not in alphabet:
            decrypted_message += char

            if show_warnings:
                print(f'Character {char} is not in the defined alphabet.\n'
                      f'Argument numbers is {numbers}.\n'
                      f'Argument symbols is {symbols}.')

        else:
            # Get the character index
            char_idx = alphabet.index(char)

            # Get the new index after shifting
            new_idx = (char_idx + key) % len(alphabet)

            # Use the new character in the encrypted message
            decrypted_message += alphabet[new_idx]

    return ''.join(decrypted_message)
            


#if __name__ == "__main__":

