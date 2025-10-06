class MainView:
    def show_welcome_menu(self):
        print("Welcome to EventLink!")
        print("What do you want to do?")
        print("0 - Login")
        print("1 - Register")
        print("2 - Exit")
        choice = input("Choose an option: ")
        return choice