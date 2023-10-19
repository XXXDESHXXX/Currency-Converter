from abc import ABC, abstractmethod
from enum import Enum

from validators import validate_password, validate_username


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


def get_menu_option() -> str:
    option = input("Choose menu option:\n1. Go to the converter menu\n2. Print conversion history\n3. Exit\n")
    if option != "1" and option != "2" and option != "3":
        print("Invalid option selected")
        return get_menu_option()
    return option

