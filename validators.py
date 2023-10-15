from constants import MIN_PASSWORD_LENGTH, PROHIBITED_PASSWORD_CHARACTERS, MIN_USERNAME_LENGTH, MAX_USERNAME_LENGTH, \
    MAX_PASSWORD_LENGTH


def validate_password(password):
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValueError(f"Password length must be more than {MIN_PASSWORD_LENGTH} symbols or equal")
    for character in PROHIBITED_PASSWORD_CHARACTERS:
        if character in password:
            prohibited_characters = ", ".join(PROHIBITED_PASSWORD_CHARACTERS)
            raise ValueError(
                f"{character} is not allowed in password,"
                f" there are such prohibited characters: {prohibited_characters}"
            )
    if len(password) > MAX_PASSWORD_LENGTH:
        raise ValueError(f"Password length must be less than {MAX_PASSWORD_LENGTH} symbols or equal")


def validate_username(username):
    if len(username) < MIN_USERNAME_LENGTH:
        raise ValueError(f"Username length must be more than {MIN_USERNAME_LENGTH} symbols or equal")
    if len(username) > MAX_USERNAME_LENGTH:
        raise ValueError(f"Username length must be less than {MAX_USERNAME_LENGTH} symbols or equal")
