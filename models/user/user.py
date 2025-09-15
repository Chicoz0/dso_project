from base_user import BaseUser
from user_status import UserStatus

class User(BaseUser):
    def __init__(self, login: str, password: str, email: str):
        super().__init__(login, password, email)   
        self.__status = UserStatus.ACTIVE

    @property
    def status(self):
        return self.__status