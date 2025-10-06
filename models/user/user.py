from models.user.base_user import BaseUser

class User(BaseUser):
    def __init__(self, username: str, password: str, email: str):
        super().__init__(username, password, email)   
        self.__status = True

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status: bool):
        if not isinstance(status, bool) or status is None:
            raise ValueError("Status must be a bool and not None.")
        if self.__status == status:
            raise f"{self.__username} status is already {'active' if status else 'inactive'}."
        else:
            self.__status == status
            return f"{self.__username} status has been changed to {'active' if status else 'inactive'}."