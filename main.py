from database import create_tables
from services.auth import create_user, log_in
from services.io import get_password, get_username, get_auth_option, AuthOptions


def main() -> None:
    create_tables()
    auth_option = get_auth_option()
    username = get_username()
    password = get_password()
    if auth_option == AuthOptions.REGISTER:
        create_user(username, password)
    user = log_in(username, password)
    while user is None:
        print("Invalid credentials")
        user = log_in(get_username(), get_password())


if __name__ == "__main__":
    main()
