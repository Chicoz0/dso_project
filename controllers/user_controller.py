from models.user.user import User
from views.login_view import LoginView
from views.register_view import RegisterView
from views.logged_user_view import LoggedUserView


class UserController():
    def __init__(self):
        self.__user_view = LoggedUserView()
        self.__login_view = LoginView()
        self.__register_view = RegisterView()

        user003 = User(username='Normal_User_3', password='user_password_3', email='user3@example.com')
        user001 = User(username='user', password='user', email='user')
        user002 = User(username='Normal_User_2', password='user_password_2', email='user2@example.com')

        self.__users = [user001, user002, user003] # Database

    @property
    def users(self):
        return self.__users

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def register_user(self, username: str, password: str, email: str) -> User:
        if self.is_username_taken(username):
            raise ValueError(f"The username '{username}' is already in use.")
        if self.is_email_taken(email):
            raise ValueError(f"The email '{email}' is already in use.")
        new_user = User(username, password, email)
        self.__users.append(new_user)
        return new_user
    
    # Checa se um username já existe no database
    def is_username_taken(self, username: str) -> bool:
        for user in self.__users:
            if user.username == username:
                return True
        return False
    
    # Checa se um email já existe no database
    def is_email_taken(self, email: str) -> bool:
        for user in self.__users:
            if user.email == email:
                return True
        return False
    
    # Acha um user pela ID
    def find_user_by_id(self, user_id: str) -> User | None:
        for user in self.__users:
            if user.id == user_id:
                return user
        return None
    
    def change_password(self, user_id: str, new_password: str, old_password: str):
        user = self.find_user_by_id(user_id)
        if user:
            user.change_password(new_password, old_password)
            return True
        return False

    def change_email(self, user_id: str, new_email: str, password_confirmation: str):
        if self.is_email_taken(new_email):
            raise ValueError(f"The email '{new_email}' is already in use.")
        user = self._find_user_by_id(user_id)
        if user:
            user.change_email(new_email, password_confirmation)
            return True
        return False

    def change_username(self, user_id: str, new_username: str, password_confirmation: str):
        if self.is_username_taken(new_username):
            raise ValueError(f"The username '{new_username}' is already in use.")
        user = self._find_user_by_id(user_id)
        if user:
            user.change_username(new_username, password_confirmation)
            return True
        return False
