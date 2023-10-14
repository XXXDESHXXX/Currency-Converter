from database import create_tables
from services.io import get_password, get_username, is_want_to_register
from services.auth import register


def main():
    create_tables()
    if is_want_to_register():
        password = get_password()
        username = get_username()
        register(username, password)


if __name__ == "__main__":
    main()
