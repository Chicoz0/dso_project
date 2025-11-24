from views.generic_view import GenericView
import FreeSimpleGUI as sg


class MainView(GenericView):
    def show_welcome_menu(self):
        layout = [
            [self.header("Welcome to EventLink!")],
            [self.title("What do you want to do?")],
            [self.radio("Login", "RD1", key="1")],
            [self.radio("Register", "RD1", key="2")],
            [self.radio("Exit", "RD1", key="0")],
            [self.button("Confirmar"), self.cancel()],
        ]
        self.window = sg.Window("EventLink!").Layout(layout)

        button, values = self.read_window()
        opcao = 0
        if values["1"]:
            opcao = 1
        if values["2"]:
            opcao = 2
        if values["0"] or button in (None, "Cancelar"):
            opcao = 0
        self.close()
        return opcao

    def show_exit_message(self):
        self.popup("Exiting EventLink. Goodbye!\n")

    def show_incorrect_value_message(self, values):
        self.popup(f"You must insert valid option {values}")
