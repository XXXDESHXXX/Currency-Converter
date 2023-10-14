from constants import PROHIBITED_PASSWORD_CHARACTERS, MAX_PASSWORD_LENGTH, MAX_USERNAME_LENGTH
from enum import Enum


class AuthOptions(Enum):
    REGISTER = 1
    LOG_IN = 2


def get_auth_option():
    answer = input("Choose the option:\n1. Register\n2. Log in\n")
    if answer != "1" and answer != "2":
        print(f"Invalid option selected")
        return get_auth_option()
    match answer:
        case "1":
            return AuthOptions.REGISTER
        case "2":
            return AuthOptions.LOG_IN


def get_password():
    joined_prohibited_password_characters = ", ".join(PROHIBITED_PASSWORD_CHARACTERS)
    password = input("Enter a password: ")
    if len(password) < MAX_PASSWORD_LENGTH:
        print(f"Password length must be more than {MAX_PASSWORD_LENGTH} symbols or equal")
        return get_password()
    for character in PROHIBITED_PASSWORD_CHARACTERS:
        if character in password:
            print(
                f"{character} is not allowed in password,"
                f" there are such prohibited characters: {joined_prohibited_password_characters}"
            )
            return get_password()
    return password


def get_username():
    username = input("Enter a username: ")
    if len(username) < MAX_USERNAME_LENGTH:
        print(f"Username length must be more than {MAX_USERNAME_LENGTH} symbols or equal")
        return get_username()
    return username
