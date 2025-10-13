from views.generic_view import GenericView


class LoggedUserView(GenericView):
    def show_logged_user_menu(self, username: str):
        print(f"\n----- User Dashboard ({username}) -----")
        print("1 - Browse Events")
        print("2 - Manage Connections")
        print("3 - Show User info")
        print("4 - Edit Profile")
        print("5 - Delete Account")
        print("0 - Logout")
        choice = super().input_int("Choose an option: ")
        return choice

    def show_error_message(self, error: Exception):
        print(f"\nError: {error}\n")

    def show_user_info_message(self, username: str, email: str):
        print(f"\nUsername: {username}")
        print(f"Email: {email}\n")

    def show_operation_done_message(self):
        print("Operation done!\n")

    def show_connections_menu(self):
        print("\n----- Connections Menu -----")
        print("1 - View My Connections")
        print("2 - View Pending Connection Requests")
        print("3 - Send a New Connection Request")
        print("0 - Return to User Dashboard")
        choice = super().input_int("Choose an option: ")
        return choice

    def show_my_connections(self, connections: list):
        # Espera que connections seja uma lista de tuplas (user_id, username)
        print("\n----- My Connections -----")
        if not connections:
            print("You don't have any accepted connections yet.")
            print("Press any key to return...")
            return None  # return None deve ser entendido pelo controlador como show_connections_menu

        for user_id, username in connections:
            print(f"ID: {user_id} - {username}")

        print("\nEnter a valid ID to view more details, or '0' to return.")
        return super().input_int(
            "Enter your choice: "
        )  # se ID correta, controlador direciona pra ConnectionView

    def show_specific_connection(
        self, connection_id: str, user1_name: str, user2_name: str
    ):
        print("\n----- Connection Details -----")
        print(f"Connection ID: {connection_id}")
        print(f"Between: {user1_name} and {user2_name}")
        print("1 - Accept Request")
        print("2 - Decline Request")
        print("0 - Return")
        choice = super().input_int("Choose an option: ")
        return choice

    def show_pending_connection_requests(self, requests: list):
        # espera que requests seja uma lista de tuplas (user_id, username)
        print("\n----- Pending Connection Requests -----")
        if not requests:
            print("You don't have any pending requests.")
            print("Press any key to return...")
            return None  # return vazio deve ser entendido pelo controlador como show_connections_menu

        for user_id, username in requests:
            print(f"ID: {user_id} - {username}")

        print("\nChoose an ID to accept/reject, or enter '0' to return.")
        return super().input_int(
            "Enter your choice: "
        )  # se ID correta, controlador direciona pra ConnectionView

    def show_new_connection_request(self):
        print("\n----- Send New Connection Request -----")
        user_id = super().input_int(
            "Enter the ID of the person you want to connect with: "
        )
        return user_id

    def show_connection_already_exists(self):
        print("\nA connection between these users already exists.")
        return self.show_new_connection_request

    def show_connection_not_found(self, connection_id: int):
        print(f"Connection with ID '{connection_id}' not found.")

    def show_edit_profile_menu(self):
        print("\n----- Edit Profile -----")
        print("1 - Change Username")
        print("2 - Change Password")
        print("3 - Change Email")
        print("0 - Return to Dashboard")
        return super().input_int("Choose an option: ")

    def prompt_new_username(self):
        print("\n----- Change Username -----")
        new_username = super().input_string("Enter new username: ")
        return new_username

    def prompt_new_password(self):
        print("\n----- Change Password -----")
        password = super().input_string("Enter your new password: ")
        return password

    def prompt_new_email(self):
        print("\n----- Change Email -----")
        new_email = super().input_string("Enter new email: ")
        return new_email
