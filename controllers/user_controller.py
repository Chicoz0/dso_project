from controllers.event_controller import EventController
from controllers.connection_controller import ConnectionController
from models.user.user import User
from views.logged_user_view import LoggedUserView
from DAOs.user_dao import UserDAO

from exceptions.generic_exceptions import NotFoundException


class UserController:
    def __init__(self, main_controller):
        self.__user_view = LoggedUserView()
        self.__main_controller = main_controller
        self.__event_controller = EventController(main_controller)
        self.__connection_controller = ConnectionController(main_controller)

        self.__user_dao = UserDAO()

    @property
    def users(self):
        return self.__user_dao.get_all()

    def login(self, username, password):
        try:
            user = self.__user_dao.get(username)
            if isinstance(user, User) and user.password == password:
                return user
        except NotFoundException:
            pass

        return None

    def load_logged_user_view(self):
        while True:
            choice = self.__user_view.show_logged_user_menu(
                self.__main_controller.logged_user.username
            )

            if choice == 0:
                self.__main_controller.logout_user()
                self.__main_controller.start()
            elif choice == 1:
                self.__event_controller.show_event_view()
            elif choice == 2:
                self.__connection_controller.load_connections_menu()
            elif choice == 3:
                self.__user_view.show_user_info_message(
                    self.__main_controller.logged_user.username,
                    self.__main_controller.logged_user.email,
                )
            elif choice == 4:
                self.load_edit_profile_view()
            elif choice == 5:
                if self.__user_view.propmt_user_yes_or_no("\nAre you sure?"):
                    self.__user_dao.remove(self.__main_controller.logged_user.username)
                    self.__main_controller.logout_user()
                    self.__user_view.show_operation_done_message()
                    self.__main_controller.start()

    def load_edit_profile_view(self):
        choice = self.__user_view.show_edit_profile_menu()

        if choice == 0:
            self.load_logged_user_view()
        elif choice == 1:
            username = self.__user_view.prompt_new_username()
            try:
                self.change_username(username)
            except ValueError as e:
                self.__user_view.show_error_message(e)
            self.__user_view.show_operation_done_message()
            self.load_edit_profile_view()

        elif choice == 2:
            password = self.__user_view.prompt_new_password()
            try:
                self.change_password(password)
                self.__user_view.show_operation_done_message()
                self.load_edit_profile_view()
            except ValueError as e:
                self.__user_view.show_error_message(e)
        elif choice == 3:
            email = self.__user_view.prompt_new_email()

            try:
                self.change_email(email)
                self.__user_view.show_operation_done_message()
                self.load_edit_profile_view()
            except ValueError as e:
                self.__user_view.show_error_message(e)

    def register_user(self, username: str, password: str, email: str) -> User:
        if self.is_username_taken(username):
            raise ValueError(f"The username '{username}' is already in use.")
        if self.is_email_taken(email):
            raise ValueError(f"The email '{email}' is already in use.")
        new_user = User(username, password, email)
        self.__user_dao.add(new_user)
        return new_user

    # Checa se um username já existe no database
    def is_username_taken(self, username: str) -> bool:
        try:
            self.__user_dao.get(username)
            return True
        except NotFoundException:
            return False

    # Checa se um email já existe no database
    def is_email_taken(self, email: str) -> bool:
        users = self.__user_dao.get_all()
        for user in users:
            if user.email == email:
                return True
        return False

    def change_password(self, new_password: str):
        user = self.__main_controller.logged_user
        if user:
            user.change_password(new_password)
            self.__user_dao.update(user)

    def change_email(self, new_email: str) -> bool:
        if self.is_email_taken(new_email):
            raise ValueError(f"The email '{new_email}' is already in use.")
        user = self.__main_controller.logged_user
        if user:
            user.email = new_email
            self.__user_dao.update(user)
            return True
        return False

    def change_username(self, new_username: str) -> bool:
        if self.is_username_taken(new_username):
            raise ValueError(f"The username '{new_username}' is already in use.")
        user = self.__main_controller.logged_user
        if user:
            old_username = user.username
            self.__user_dao.remove(old_username)
            user.username = new_username
            self.__user_dao.add(user)
            return True
        return False

    def find_user_by_username(self, username: str) -> User | None:
        try:
            return self.__user_dao.get(username)
        except NotFoundException as e:
            self.__user_view.show_error_message(e)
            return None
