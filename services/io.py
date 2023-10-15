from enum import Enum

from validators import validate_password, validate_username


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
    password = input("Enter a password: ")
    try:
        validate_password(password)
    except ValueError as error:
        print(error)
        get_password()
    return password


def get_username():
    username = input("Enter a username: ")
    try:
        validate_username(username)
    except ValueError as error:
        print(error)
        get_username()
    return username
