from constants import PROHIBITED_PASSWORD_CHARACTERS, MAX_PASSWORD_LENGTH, MAX_USERNAME_LENGTH


def is_want_to_register():
    answer = input("Choose the option:\n1. Register\n2. Log in\n")
    if answer != "1" and answer != "2":
        print(f"Invalid option selected")
        return is_want_to_register()
    match answer:
        case "1":
            return True
        case "2":
            return False


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
