from views.generic_view import GenericView
import FreeSimpleGUI as sg


class MainView(GenericView):
    def show_welcome_menu(self):
        # print("\nWelcome to EventLink!")
        # print("What do you want to do?")
        # print("1 - Login")
        # print("2 - Register")
        # print("0 - Exit")
        # choice = super().input_int("Choose an option: ")
        # return choice

        layout = [
            [sg.Text('Welcome to EventLink!', font=("Helvica",25))],
            [sg.Text('What do you want to do?', font=("Helvica",15))],
            [sg.Radio('Login',"RD1", key='1')],
            [sg.Radio('Register',"RD1", key='2')],
            [sg.Radio('Exit',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('EventLink!').Layout(layout)

        button, values = self.window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao


    def show_exit_message(self):
        self.popup("Exiting EventLink. Goodbye!\n")

    def show_incorrect_value_message(self, values):
        self.popup(f"You must insert valid option {values}")
