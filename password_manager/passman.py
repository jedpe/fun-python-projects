import secrets
import string
import types


# Random password generator
def random_password(length, upper=True, lower=True, numbers=True, symbols=True):
    """
        Generate a random password of the given length using allowed characters.

        Parameters
        ----------
        length: int
            Number of characters to be used for the password.

        upper: bool, default=True
            If True, the generated password will contain upper case characters.

        lower: bool, default=True
            If True, the generated password will contain lower case characters.

        numbers: bool, default=True
            If True, the generated password will contain numbers.

        symbols: bool or list, default=True
            If True, the generated password will contain symbols. If set to False,
            the password will contain no symbols. Alternatively, use a list to 
            specify the symbols the password is allowed to contain.
    """

    # Determine allowed characters
    characters = []
    if upper:
        # Add upper case letters
        characters.append(string.ascii_uppercase)

    if lower:
        # Add lower case letters
        characters.append(string.ascii_lowercase)

    if numbers:
        # Add numbers
        characters.append(string.digits)

    if isinstance(symbols, types.BooleanType):
        # Add all symbols
        characters.append(string.punctuation)

    elif isinstance(symbols, types.ListType):
        # Add specified symbols
        characters += symbols

    # Generate a random choice of characters
    pswd = [secrets.choice(characters) for c in range(length)]

    return ''.join(pswd)
