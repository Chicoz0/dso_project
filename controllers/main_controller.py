import sys

from views.main_view import MainView
from views.login_view import LoginView
from views.register_view import RegisterView

from controllers.user_controller import UserController


class MainController:
    def __init__(self):
        self.__logged_user = None
        self.__main_view = MainView()
        self.__login_view = LoginView()
        self.__register_view = RegisterView()
        self.__user_controller = UserController(self)

    @property
    def logged_user(self):
        return self.__logged_user

    # Crime temporário
    @property
    def user_controller(self):
        return self.__user_controller

    def start(self):
        while True:
            choice = self.__main_view.show_welcome_menu()
            if choice == 0:
                self.__main_view.show_exit_message()
                sys.exit()
            elif choice == 1:
                self.handle_login()
            elif choice == 2:
                self.handle_register()
            else:
                self.__main_view.show_incorrect_value_message([0, 1, 2])

    def logout_user(self):
        self.__logged_user = None

    def handle_login(self):
        username, password = self.__login_view.show_login_menu()
        self.__login_view.show_login_attempt_message(username)

        user = self.__user_controller.login(username, password)

        if user:
            self.__logged_user = user
            self.__login_view.login_success()
            self.__user_controller.load_logged_user_view()
        else:
            self.__login_view.show_login_attempt_fail_message()
            return

    def handle_register(self):
        email, username, password = self.__register_view.show_register_menu()

        try:
            user = self.__user_controller.register_user(username, password, email)
            self.__register_view.show_register_success_message(user.username)
        except ValueError as e:
            self.__register_view.show_register_error(e)
