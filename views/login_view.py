from views.generic_view import GenericView


class LoginView(GenericView):
    def login_success(self):
        print("\nLogin successful!")

    def show_login_attempt_fail_message(self):
        print("\nError while trying to login, verify username or password!\n")

    def show_login_menu(self):
        print("\n----- User Login -----")
        username = super().input_string("Enter your username: ")
        password = super().input_string("Enter your password: ")
        return username, password

    def show_login_attempt_message(self, username: str):
        print(f"\nAttempting to log in with username: {username}\n")
