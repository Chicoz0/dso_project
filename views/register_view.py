from views.generic_view import GenericView
import FreeSimpleGUI as sg


class RegisterView(GenericView):
    def show_register_menu(self):
        layout = [
            [sg.Text("-------- User Register ----------", font=("Helvica", 25))],
            [sg.Text("Email:", size=(15, 1)), sg.InputText("", key="email")],
            [sg.Text("Username:", size=(15, 1)), sg.InputText("", key="username")],
            [sg.Text("Password:", size=(15, 1)), sg.InputText("", key="password")],
            [sg.Button("Confirm"), sg.Cancel("Cancel")],
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
