class RegisterView:
    def show_register_menu(self):
        print("\n----- User Registration -----")
        email = input("Enter your email: ")
        username = input("Enter a new username: ")
        password = input("Create a password: ")
        return email, username, password
