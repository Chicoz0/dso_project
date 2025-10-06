from views.main_view import MainView
from views.login_view import LoginView
from views.register_view import RegisterView
from views.logged_user_view import LoggedUserView
from views.logged_admin_view import LoggedAdminView
from views.connection_view import ConnectionView

from models.user.user import User
from models.user.admin_user import AdminUser

from controllers.user_controller import UserController
from controllers.admin_controller import AdminController


class MainController:
    def __init__(self):
        self.__main_view = MainView()
        self.__login_view = LoginView()
        self.__register_view = RegisterView()
        self.__logged_user_view = LoggedUserView()
        self.__logged_admin_view = LoggedAdminView()
        self.__connection_view = ConnectionView()

        
        self.__user_controller = UserController()
        self.__admin_controller = AdminController()

        # self.__users = UserController.users()
        # self.__admins = AdminController.admins()
        
    def start(self):
        while True:
            choice = self.__main_view.show_welcome_menu()
            if choice == '0':
                self.handle_login()
            elif choice == '1':
                self.handle_register()
            elif choice == '2':
                print("Exiting EventLink. Goodbye!")
                break
            else:
                print("You must insert a value between 0-2.")
    
    def handle_login(self):
        username, password = self.__login_view.show_login_menu()
        print(f"Attempting to log in with username: {username}")

        user = self.__user_controller.login(username, password)

        if user:
            self.__logged_user_view.show_logged_user_menu()
        else:
            print("Login Failed!")
            self.handle_login()

    def handle_register(self):
        email, username, password = self.__register_view.show_register_menu()

        try:
            user = self.__user_controller.register_user(username, password, email)
            print(f"User with username {user.username} was created!")
        except ValueError as e:
            print(f"Error while creating user: {e}")

