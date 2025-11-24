from abc import ABC, abstractmethod
from DAOs.ids_dao import UniversalID


class BaseUser(ABC):
    @abstractmethod
    def __init__(self, username: str, password: str, email: str):
        if not isinstance(username, str) or username is None:
            raise ValueError("Username must be a string and not null")
        if not isinstance(password, str) or password is None:
            raise ValueError("Password must be a string and not null")
        if not isinstance(email, str) or email is None:
            raise ValueError("E-mail must be a string and not null")
        self.__id = UniversalID().get_id()
        self.__password = password
        self.__email = email
        self.__username = username

    @property
    def id(self):
        return self.__id

    @property
    def email(self):
        return self.__email

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    def change_password(self, new_password: str):
        if not isinstance(new_password, str) or new_password is None:
            raise ValueError("New password must be a string and not null.")
        self.__password = new_password

    def change_email(self, new_email: str):
        if not isinstance(new_email, str) or new_email is None:
            raise ValueError("New email must be a string and not null")
        self.__email = new_email

    def change_username(self, new_username: str):
        if not isinstance(new_username, str) or new_username is None:
            raise ValueError("New username must be a string and not null")
        self.__username = new_username
