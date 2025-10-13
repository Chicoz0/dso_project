class LoggedUserView:
    def show_logged_user_menu(self, username: str):
        print(f"\n----- User Dashboard ({username}) -----")
        print("1 - Browse Events")
        print("2 - Manage Connections")
        print("3 - Show User info")
        print("4 - Edit Profile")
        print("5 - Delete Account")
        print("0 - Logout")
        choice = input("Choose an option: ")
        return choice

    def propmt_user_for_confirmation(self):
        print("\nAre you sure?")
        print("1 - Yes")
        print("2 - No")
        choice = input("Choose an option: ")
        return choice

    def show_error_message(self, error: Exception):
        print(f"\nError: {error}\n")

    def show_user_info_message(self, username: str, email: str):
        print(f"\nUsername: {username}")
        print(f"Email: {email}\n")

    def show_operation_done_message(self):
        print("Operation done!\n")

    def show_all_events(self, events: list):
        #  pede ao controlador a lista de todos eventos
        #  espera como retorno uma [] de tuplas [(event_id_1, name_1),
        #  (event_id_2, name_2)...]
        print("\n----- All Available Events -----")
        if not events:
            print("There are no events available at the moment.")
            print("Press any key to return...")
            return None  # return None deve ser entendido pelo controlador como show_logged_user_menu

        for event_id, event_name in events:
            print(f"ID: {event_id} - {event_name}")

        print(
            "\nEnter a valid ID to view more details, or '0' to return to 'User Dashboard'."
        )
        return input(
            "Enter your choice: "
        )  # add opcao de retornar ao show_logged_user_menu

    def show_attending_events(self, my_events: list):
        #  pede ao controlador a lista de eventos com presença do user
        #  espera como retorno uma [] de tuplas [(event_id_1, name_1),
        #  (event_id_2, name_2)...]
        print("\n----- My Confirmed Events -----")
        if not my_events:
            print("You have not confirmed attendance for any events yet.")
            print("Press any key to return...")
            return None  # return None deve ser entendido pelo controlador como show_logged_user_menu

        for event_id, event_name in my_events:
            print(f"ID: {event_id} - {event_name}")

        print(
            "\nEnter a valid ID to view more details, or '0' to return to 'User Dashboard'."
        )
        return input("Enter your choice: ")

    def show_connections_menu(self):
        print("\n----- Connections Menu -----")
        print("1 - View My Connections")
        print("2 - View Pending Connection Requests")
        print("3 - Send a New Connection Request")
        print("0 - Return to User Dashboard")
        choice = input("Choose an option: ")
        return choice

    def show_my_connections(self, connections: list):
        # Espera que connections seja uma lista de tuplas (user_id, username)
        print("\n----- My Connections -----")
        if not connections:
            print("You don't have any accepted connections yet.")
            print("Press any key to return...")
            return None  # return None deve ser entendido pelo controlador como show_connections_menu

        for user_id, username in connections:
            print(f"ID: {user_id} - {username}")

        print("\nEnter a valid ID to view more details, or '0' to return.")
        return input(
            "Enter your choice: "
        )  # se ID correta, controlador direciona pra ConnectionView

    def show_pending_connection_requests(self, requests: list):
        # espera que requests seja uma lista de tuplas (user_id, username)
        print("\n----- Pending Connection Requests -----")
        if not requests:
            print("You don't have any pending requests.")
            print("Press any key to return...")
            return None  # return vazio deve ser entendido pelo controlador como show_connections_menu

        for user_id, username in requests:
            print(f"ID: {user_id} - {username}")

        print("\nChoose an ID to accept/reject, or enter '0' to return.")
        return input(
            "Enter your choice: "
        )  # se ID correta, controlador direciona pra ConnectionView

    def show_new_connection_request(self):
        print("\n----- Send New Connection Request -----")
        user_id = input("Enter the ID of the person you want to connect with: ")
        return user_id

    def show_edit_profile_menu(self):
        print("\n----- Edit Profile -----")
        print("1 - Change Username")
        print("2 - Change Password")
        print("3 - Change Email")
        print("0 - Return to Dashboard")
        return input("Choose an option: ")

    def prompt_new_username(self):
        print("\n----- Change Username -----")
        new_username = input("Enter new username: ")
        return new_username

    def prompt_new_password(self):
        print("\n----- Change Password -----")
        password = input("Enter your new password: ")
        return password

    def prompt_new_email(self):
        print("\n----- Change Email -----")
        new_email = input("Enter new email: ")
        return new_email
