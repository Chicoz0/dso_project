from views.generic_view import GenericView


class MainView(GenericView):
    def show_welcome_menu(self):
        print("\nWelcome to EventLink!")
        print("What do you want to do?")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")
        choice = super().input_int("Choose an option: ")
        return choice

    def show_exit_message(self):
        print("Exiting EventLink. Goodbye!\n")

    def show_incorrect_value_message(self, values):
        print(f"You must insert valid option {values}")
