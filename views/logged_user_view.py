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

    # ------ Connection related section -------
    def show_connections_menu(self):
        print("\n----- Connections Menu -----")
        print("1 - View Accepted Connections")
        print("2 - View Pending Connection Requests")
        print("3 - Send a New Connection Request")
        print("0 - Return to User Dashboard")
        choice = super().input_int("Choose an option: ")
        return choice

    def show_accepted_connections(self, connections: list):
        # Espera que connections seja uma lista de tuplas (connection_id, username)
        print("\n----- My Connections -----\n")
        if not connections:
            print("You don't have any accepted connections yet.")
            input("\nPress any key to return.")
            return None

        for connection_id, username in connections:
            print(f"ID: {connection_id} - Username: {username}")
        
        print("\nEnter a valid ID to dismiss a connection, or '0' to return.")
        return super().input_int("Enter your choice: ")

    def show_accepted_connection(
        self, connection_id: int, user1_username: str, user2_username: str):
        print("\n----- Connection Details -----")
        print(f"Connection ID: {connection_id}")
        print(f"Between: {user1_username} and {user2_username}")
        print("1 - Dismiss Connection")
        print("0 - Return")
        choice = super().input_int("Choose an option: ")
        return choice

    def show_pending_connection_requests(self, requests: list):
        print("\n----- Pending Connection Requests -----")
        if not requests:
            print("You don't have any pending requests.")
            input("\nPress any key to return...")
            return None

        for connection_id, username in requests:
            print(f"Connection ID: {connection_id} - Username: {username}")

        print("\nChoose a ID to accept/reject, or enter '0' to return.")
        return super().input_int("Enter your choice: ")

    def show_accept_reject_connection_menu(self, username: str):
        print(f"\nConnection Request from: {username}")
        print("1 - Accept")
        print("2 - Reject")
        print("0 - Return")
        return super().input_int("Choose an option: ")

    def show_new_connection_request(self):
        print("\n----- Send New Connection Request -----")
        user_username = super().input_string("Enter the Username of the user you want to connect with or enter '0' to Return: ")
        return user_username

    def show_connection_already_exists(self):
        print("\nA connection between these users already exists.")

    def show_connection_not_found(self, connection_id: int):
        print(f"Connection with ID '{connection_id}' not found.")

    # ----- Edit Profile related section -----
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
