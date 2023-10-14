from database import create_tables
from services.io import get_password, get_username, get_auth_option, AuthOptions
from services.auth import register


def main():
    create_tables()
    match get_auth_option():
        case AuthOptions.REGISTER:
            password = get_password()
            username = get_username()
            register(username, password)
        case AuthOptions.LOG_IN:
            pass


if __name__ == "__main__":
    main()
