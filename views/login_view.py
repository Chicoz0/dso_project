class LoginView:
    def show_login_menu(self):
        print("\n----- User Login -----")        
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return username, password