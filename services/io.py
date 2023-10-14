from constants import PROHIBITED_PASSWORD_CHARACTERS, MAX_PASSWORD_LENGTH, MAX_USERNAME_LENGTH


def get_password():
    joined_prohibited_password_characters = ", ".join(PROHIBITED_PASSWORD_CHARACTERS)
    password = input("Enter a password: ")
    if len(password) <= MAX_PASSWORD_LENGTH:
        raise ValueError(f"Password length must be more than {MAX_PASSWORD_LENGTH} symbols or equal")
    for character in PROHIBITED_PASSWORD_CHARACTERS:
        if character in password:
            raise ValueError(
                f"{character} is not allowed in password,"
                f" there are such prohibited characters: {joined_prohibited_password_characters}"
            )
    return password


def get_username():
    username = input("Enter a username: ")
    if len(username) <= MAX_USERNAME_LENGTH:
        raise ValueError(f"Username length must be more than {MAX_USERNAME_LENGTH} symbols or equal")
    return username
