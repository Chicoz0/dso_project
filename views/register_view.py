from views.generic_view import GenericView


class RegisterView(GenericView):
    def show_register_menu(self):
        print("\n----- User Registration -----")
        email = super().input_string("Enter your email: ")
        username = super().input_string("Enter a new username: ")
        password = super().input_string("Create a password: ")
        return email, username, password

    def show_register_success_message(self, username: str):
        print(f"User with username {username} was created!\n")

    def show_register_error(self, error: Exception):
        print(f"Error while creating user: {error}\n")
