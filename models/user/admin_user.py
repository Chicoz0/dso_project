from base_user import BaseUser

class AdminUser(BaseUser):
    def __init__(self, login: str, password: str, email: str, is_admin: bool = True):
        super().__init__(login, password, email)
        self.__is_admin = is_admin

    @property
    def is_admin(self):
        return self.__is_admin