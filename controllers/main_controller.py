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

        self.__users = UserController.users()
        self.__admins = AdminController.admins()
        
        # mockdata
        admin001 = AdminUser(username='Admin_User_1', password='admin_password_1', email='admin1@example.com')
        admin002 = AdminUser(username='Admin_User_2', password='admin_password_2', email='admin2@example.com')
        user001 = User(username='Normal_User_1', password='user_password_1', email='user1@example.com')
        user002 = User(username='Normal_User_2', password='user_password_2', email='user2@example.com')
        user003 = User(username='Normal_User_3', password='user_password_3', email='user3@example.com')
        user004 = User(username='Normal_User_4', password='user_password_4', email='user4@example.com')
        user005 = User(username='Normal_User_5', password='user_password_5', email='user5@example.com')
        user006 = User(username='Normal_User_6', password='user_password_6', email='user6@example.com')
        user007 = User(username='Normal_User_7', password='user_password_7', email='user7@example.com')
        user008 = User(username='Normal_User_8', password='user_password_8', email='user8@example.com')
        user009 = User(username='Normal_User_9', password='user_password_9', email='user9@example.com')
        user010 = User(username='Normal_User_10', password='user_password_10', email='user10@example.com')
        user011 = User(username='Normal_User_11', password='user_password_11', email='user11@example.com')
        user012 = User(username='Normal_User_12', password='user_password_12', email='user12@example.com')

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
        # ...

    def handle_register(self):
        email, username, password, password_confirmation = self.__register_view.show_register_menu()
        #....