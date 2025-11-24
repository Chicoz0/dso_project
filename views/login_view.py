import FreeSimpleGUI as sg
from views.generic_view import GenericView


class LoginView(GenericView):
    def login_success(self):
        self.popup("\nLogin successful!")

    def show_login_attempt_fail_message(self):
        self.popup("\nError while trying to login, verify username or password!\n")

    def show_login_menu(self):
        layout = [
            [self.header("-------- User Login ----------")],
            [
                self.input_title("Enter username:"),
                self.input_text("username"),
            ],
            [
                self.input_title("Enter password:"),
                self.input_text("password"),
            ],
            [self.confirm()],
        ]
        self.window = sg.Window("EventLink").Layout(layout)

        _, values = self.read_window()
        username = values["username"]
        password = values["password"]

        self.close()
        return username, password

    def show_login_attempt_message(self, username: str):
        self.popup(f"\nAttempting to log in with username: {username}\n")
