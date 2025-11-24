from views.generic_view import GenericView
import FreeSimpleGUI as sg


class RegisterView(GenericView):
    def show_register_menu(self):
        layout = [
            [self.header("-------- User Register ----------")],
            [self.input_title("Email:"), self.input_text("email")],
            [self.input_title("Username:"), self.input_text("username")],
            [self.input_title("Password:"), self.input_text("password")],
            [self.confirm()],
        ]
        self.window = sg.Window("EventLink").Layout(layout)

        _, values = self.read_window()
        email = values["email"]
        username = values["username"]
        password = values["password"]

        self.close()
        return email, username, password

    def show_register_success_message(self, username: str):
        self.popup(f"User with username {username} was created!\n")

    def show_register_error(self, error: Exception):
        self.popup(f"Error while creating user: {error}\n")
