from abc import ABC, abstractmethod

class BaseUser(ABC):
    @abstractmethod
    def __init__(self, id: int, login: str, password_token: str, email: str):
        self.__id = None
        self.__login = ""
        self.__password_token = ""
        self.__email = ""

        if isinstance(id, int) and id is not None:
            self.__id = id
        if isinstance(login, str) and login is not None:
            self.__login = login
        if isinstance(password_token, str) and password_token is not None:
            self.__password_token = password_token
        if isinstance(email, str) and email is not None:
            self.__email = email

    @property
    def id(self):
        return self._id

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password_token

    @property
    def email(self):
        return self._email

    def change_password(self, new_password_token: str):
        if isinstance(new_password_token, str) and new_password_token is not None:
            self.__password_token = new_password_token
            print(f"Password for {self.__login} has been changed.")

    def change_email(self, new_email: str):
        if isinstance(new_email, str) and new_email is not None:
            self.__email = new_email
            print(f"Email for {self.__login} has been changed to {self.__email}.")