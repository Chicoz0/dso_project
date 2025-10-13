from controllers.event_controller import EventController
from models.user.user import User
from views.logged_user_view import LoggedUserView


class UserController:
    def __init__(self, main_controller):
        self.__user_view = LoggedUserView()
        self.__main_controller = main_controller
        self.__event_controller = EventController(main_controller)

        user003 = User(
            username="Normal_User_3",
            password="user_password_3",
            email="user3@example.com",
        )
        user001 = User(username="user", password="user", email="user")
        user002 = User(
            username="Normal_User_2",
            password="user_password_2",
            email="user2@example.com",
        )

        self.__users = [user001, user002, user003]  # Database

    @property
    def users(self):
        return self.__users

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def show_logged_user_view(self):
        while True:
            choice = self.__user_view.show_logged_user_menu(
                self.__main_controller.logged_user.username
            )

            if choice == "0":
                self.__main_controller.logout_user()
                self.__main_controller.start()
            elif choice == "1":
                self.__event_controller.show_event_view()
            elif choice == "2":
                # ToDo connections
                pass
            elif choice == "3":
                self.__user_view.show_user_info_message(
                    self.__main_controller.logged_user.username,
                    self.__main_controller.logged_user.email,
                )
            elif choice == "4":
                self.load_edit_profile_view()
            elif choice == "5":
                choice = self.__user_view.propmt_user_for_confirmation()
                if choice == "1":
                    self.users.remove(self.__main_controller.logged_user)
                    self.__main_controller.logout_user()
                    self.__user_view.show_operation_done_message()
                    self.__main_controller.start()

    def load_edit_profile_view(self):
        choice = self.__user_view.show_edit_profile_menu()

        if choice == "0":
            self.show_logged_user_view()
        elif choice == "1":
            username = self.__user_view.prompt_new_username()
            try:
                self.change_username(username)
            except ValueError as e:
                self.__user_view.show_error_message(e)
            self.__user_view.show_operation_done_message()
            self.load_edit_profile_view()

        elif choice == "2":
            password = self.__user_view.prompt_new_password()
            try:
                self.change_password(password)
                self.__user_view.show_operation_done_message()
                self.load_edit_profile_view()
            except ValueError as e:
                self.__user_view.show_error_message(e)
        elif choice == "3":
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
    def find_user_by_id(self, user_id: int) -> User | None:
        for user in self.__users:
            if user.id == user_id:
                return user
        return None

    def change_password(self, new_password: str):
        if self.__main_controller.logged_user:
            self.__main_controller.logged_user.change_password(new_password)

    def change_email(self, new_email: str):
        if self.is_email_taken(new_email):
            raise ValueError(f"The email '{new_email}' is already in use.")
        if self.__main_controller.logged_user:
            self.__main_controller.logged_user.change_email(new_email)
            return True
        return False

    def change_username(self, new_username: str):
        if self.is_username_taken(new_username):
            raise ValueError(f"The username '{new_username}' is already in use.")

        if self.__main_controller.logged_user:
            self.__main_controller.logged_user.change_username(new_username)
            return True
        return False
