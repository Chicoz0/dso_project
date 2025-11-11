import FreeSimpleGUI as sg
from views.generic_view import GenericView


class LoginView(GenericView):
        #     layout = [
        #   [sg.Text('-------- User Register ----------', font=("Helvica", 25))],
        #   [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
        #   [sg.Text('Username:', size=(15, 1)), sg.InputText('', key='username')],
        #   [sg.Text('Password:', size=(15, 1)), sg.InputText('', key='password')],
        #   [sg.Button('Confirm'), sg.Cancel('Cancel')]
        # ]
        # self.window = sg.Window('EventLink').Layout(layout)
        #
        # _, values = self.open()
        # email = values['email']
        # username = values['username']
        # password = values['password']


    def login_success(self):
        self.popup("\nLogin successful!")

    def show_login_attempt_fail_message(self):
        self.popup("\nError while trying to login, verify username or password!\n")

    def show_login_menu(self):
        layout = [
          [sg.Text('-------- User Login ----------', font=("Helvica", 25))],
          [sg.Text('Enter username:', size=(15, 1)), sg.InputText('', key='username')],
          [sg.Text('Enter password:', size=(15, 1)), sg.InputText('', key='password')],
          [sg.Button('Confirm'), sg.Cancel('Cancel')]
        ]
        self.window = sg.Window('EventLink').Layout(layout)

        _, values = self.open()
        username = values['username']
        password = values['password']

        # self.popup("\n----- User Login -----")
        # username = super().input_string("Enter your username: ")
        # password = super().input_string("Enter your password: ")
        self.close()
        return username, password

    def show_login_attempt_message(self, username: str):
        self.popup(f"\nAttempting to log in with username: {username}\n")
