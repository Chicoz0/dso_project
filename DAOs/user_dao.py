from DAOs.dao import DAO
from models.user.user import User

class UserDAO(DAO):
    def __init__(self):
        super().__init__('data/users.pkl')

    def add(self, user: User):
        if((user is not None) and isinstance(user, User) and isinstance(user.username, str)):
            super().add(user.username, user)

    def update(self, user: User):
        if((user is not None) and isinstance(user, User) and isinstance(user.username, str)):
            super().update(user.username, user)

    def get(self, username: str):
        if isinstance(username, str):
            return super().get(username)

    def remove(self, username: str):
        if(isinstance(username, str)):
            return super().remove(username)
