class RegisterView:
    def show_register_menu(self):
        print("\n----- User Registration -----")
        email = input("Enter your email: ")
        username = input("Enter a new username: ")
        password = input("Create a password: ")
        return email, username, password

    def show_register_success_message(self, username: str):
        print(f"User with username {username} was created!\n")

    def show_register_error(self, error: Exception):
        print(f"Error while creating user: {error}\n")
