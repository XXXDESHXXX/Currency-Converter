from datetime import datetime

from database import create_tables
from services.api import FreeCurrencyAPI
from services.auth import create_user, log_in
from services.conversation_history import save_conversation
from services.converter import CurrencyConverter
from services.io import AuthIO, is_want_to_register, get_menu_option, get_from_currency, get_to_currency, get_amount, \
    MenuOptions, show_conversation_history


def main() -> None:
    create_tables()

    auth_io = AuthIO()
    if is_want_to_register():
        print("Registration")
        create_user(auth_io.get_username(), auth_io.get_password())

    print("Log in")
    user = log_in(auth_io)

    while True:
        menu_option = get_menu_option()
        match menu_option:
            case MenuOptions.CONVERTER_MENU:
                from_currency = get_from_currency()
                to_currency = get_to_currency()
                amount = get_amount()
                try:
                    currency_converter = CurrencyConverter(
                        FreeCurrencyAPI(),
                        from_currency,
                        to_currency,
                        amount,
                    )
                    save_conversation(from_currency, to_currency, float(amount), datetime.now(), user[0])
                    print(currency_converter.convert())
                except KeyError:
                    print("Invalid currency code")
            case MenuOptions.PRINT_CONVERSION_HISTORY:
                show_conversation_history(user[0])
            case MenuOptions.EXIT:
                exit()


if __name__ == "__main__":
    main()
