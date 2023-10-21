from abc import ABC, abstractmethod
from enum import Enum

from humanize import naturaldate

from services.selectors.conversation_history import get_conversation_history
from validators import validate_password, validate_username, validate_amount


class AbstractAuthIO(ABC):
    @abstractmethod
    def get_username(self):
        pass

    @abstractmethod
    def get_password(self):
        pass


class AuthIO(AbstractAuthIO):
    def get_username(self) -> str:
        username = input("Enter a username: ")
        try:
            validate_username(username)
        except ValueError as error:
            print(error)
            self.get_username()
        return username

    def get_password(self) -> str:
        password = input("Enter a password: ")
        try:
            validate_password(password)
        except ValueError as error:
            print(error)
            self.get_password()
        return password


def is_want_to_register() -> bool:
    answer = input("Choose the option:\n1. Register\n2. Log in\n")
    if answer != "1" and answer != "2":
        print(f"Invalid option selected")
        return is_want_to_register()
    return answer == "1"


class MenuOptions(Enum):
    CONVERTER_MENU = 1
    PRINT_CONVERSION_HISTORY = 2
    EXIT = 3


def get_menu_option() -> MenuOptions:
    option = input("Choose menu option:\n1. Go to the converter menu\n2. Print conversion history\n3. Exit\n")
    if option != "1" and option != "2" and option != "3":
        print("Invalid option selected")
        return get_menu_option()
    options_map = {
        "1": MenuOptions.CONVERTER_MENU,
        "2": MenuOptions.PRINT_CONVERSION_HISTORY,
        "3": MenuOptions.EXIT,
    }
    return options_map[option]


def get_from_currency() -> str:
    return input("Enter the currency code you want to convert from: ")


def get_to_currency() -> str:
    return input("Enter the currency code you want to convert to: ")


def get_amount() -> str:
    amount = input("Enter the amount of currency you want to convert: ")
    try:
        validate_amount(amount)
    except ValueError:
        print("Please enter a valid amount.")
        return get_amount()
    return amount


def show_conversation_history(user_id: int) -> None:
    user_conversations = get_conversation_history(user_id)
    for i, conversation in enumerate(user_conversations, start=1):
        print(
            f"""
            {i}. {conversation.from_currency} - {conversation.to_currency}
            Amount is {conversation.amount}
            Date of creation: {naturaldate(conversation.created_at)}.
            """
        )
    else:
        print("There is no previous conversations")
