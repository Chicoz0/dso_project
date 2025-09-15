from abc import ABC, abstractmethod
from utils.id import generate_id

class BaseUser(ABC):
    @abstractmethod
    def __init__(self, login, password, email):
        if not isinstance(login, str) or login is None:
            raise ValueError("login must be a string and not null")        
        if not isinstance(password, str) or password is None:
            raise ValueError("password must be a string and not null")
        if not isinstance(email, str) or email is None:
            raise ValueError("email must be a string and not null")
        self.__id = generate_id()
        self.__password = password
        self.__login = login
        self.__email = email

    @property
    def id(self):
        return self.__id

    @property
    def login(self):
        return self.__login

    @property
    def email(self):
        return self.__email

    # Most likely we will use bcrypt in the future to handle passwords
    def change_password(self, new_password: str):
        if not isinstance(new_password, str) or new_password is None:
            raise ValueError("New password must be a string and not null")
        self.__password = new_password
        print(f"Password for {self.__login} altered.")

    def change_email(self, new_email: str):
        if not isinstance(new_email, str) or new_email is None:
            raise ValueError("New email must be a string and not null")
        self.__email = new_email
        print(f"Email for {self.__login} altered to {self.__email}.")