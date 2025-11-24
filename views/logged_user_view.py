import FreeSimpleGUI as sg

from views.generic_view import GenericView


class LoggedUserView(GenericView):
    def show_logged_user_menu(self, username: str):
        layout = [
            [self.header(f"----- User Dashboard {username} -----")],
            [self.title("What do you want to do?")],
            [self.radio("Browse Events", "RD1", key="1")],
            [self.radio("Manage Connections", "RD1", key="2")],
            [self.radio("Show User info", "RD1", key="3")],
            [self.radio("Edit profile", "RD1", key="4")],
            [self.radio("Delete Account", "RD1", key="5")],
            [self.radio("Exit", "RD1", key="0")],
            [self.confirm(), self.cancel()],
        ]
        self.window = sg.Window("EventLink!").Layout(layout)

        button, values = self.read_window()
        opcao = 0
        if values["1"]:
            opcao = 1
        if values["2"]:
            opcao = 2
        if values["3"]:
            opcao = 3
        if values["3"]:
            opcao = 3
        if values["4"]:
            opcao = 4
        if values["5"]:
            opcao = 5
        if values["0"] or button in (None, "Cancelar"):
            opcao = 0
        self.close()
        return opcao

    def show_error_message(self, error: Exception):
        self.popup(f"\nError: {error}\n")

    def show_user_info_message(self, username: str, email: str):
        self.popup(f"\nUsername: {username}\nEmail: {email}")

    def show_operation_done_message(self):
        self.popup("Operation done!\n")

    # ------ Connection related section -------
    def show_connections_menu(self):
        layout = [
            [self.header(f"----- Connection Menu  -----")],
            [self.title("What do you want to do?")],
            [self.radio("View Connections", "RD1", key="1")],
            [self.radio("View Pending Connections Request", "RD1", key="2")],
            [self.radio("Send a New Connection Request", "RD1", key="3")],
            [self.confirm(), self.cancel()],
        ]
        self.window = sg.Window("EventLink!").Layout(layout)

        button, values = self.read_window()
        self.close()
        opcao = 0
        if values["1"]:
            opcao = 1
        if values["2"]:
            opcao = 2
        if values["3"]:
            opcao = 3
        if button in (None, "Cancel"):
            opcao = 0
        return opcao

    def show_accepted_connections(self, connections: list):
        if not connections:
            super().show_message("You don't have any accepted connections yet.")
            return None

        msg = ""
        for connection_id, username in connections:
            msg += f"ID: {connection_id} - Username: {username}\n"

        self.popup_scrolled(msg, title="My Connections")

        return super().input_int("Enter the ID to dismiss (or 0 to return):")

    def show_accepted_connection(self, connection_id: int, user1: str, user2: str):
        msg = (
            f"Connection ID: {connection_id}\n"
            f"Between: {user1} and {user2}\n\n"
            f"Do you want to DISMISS (remove) this connection?"
        )

        should_dismiss = super().propmt_user_yes_or_no(msg)
        return 1 if should_dismiss else 0

    def show_pending_connection_requests(self, requests: list):
        if not requests:
            super().show_message("You don't have any pending requests.")
            return None

        msg = ""
        for connection_id, username in requests:
            msg += f"Connection ID: {connection_id} - Username: {username}\n"

        self.popup_scrolled(msg, title="Pending Requests")

        return super().input_int(
            "Choose an ID to accept/reject, or enter '0' to return."
        )

    def show_accept_reject_connection_menu(self, username: str):
        layout = [
            [self.header(f"Connection Request from: {username}")],
            [self.title("What do you want to do?")],
            [
                self.button_key("Accept", key="1"),
                self.button_key("Reject", key="2"),
                self.button_key("Return", key="0"),
            ],
        ]
        self.window = sg.Window("Process Request").Layout(layout)
        button, _ = self.read_window()
        self.close()

        if button in (None, "Return"):
            return 0
        return int(button)

    def show_new_connection_request(self):
        user_username = super().input_string(
            "Enter the username of the user you want to connect with:"
        )
        if not user_username or user_username == "0":
            return "0"

        return user_username

    def show_connection_already_exists(self):
        super().show_message("A connection between these users already exists.")

    def show_connection_not_found(self, connection_id: int):
        super().show_message(f"Connection with ID '{connection_id}' not found.")

    # ----- Edit Profile related section -----
    def show_edit_profile_menu(self):
        layout = [
            [self.header(f"----- Edit Profile -----")],
            [self.radio("Change Username", "RD1", key="1")],
            [self.radio("Change Password", "RD1", key="2")],
            [self.radio("Change Email", "RD1", key="3")],
            [self.confirm(), self.cancel()],
        ]
        self.window = sg.Window("EventLink!").Layout(layout)

        button, values = self.read_window()
        opcao = 0
        if values["1"]:
            opcao = 1
        if values["2"]:
            opcao = 2
        if values["3"]:
            opcao = 3
        if button in (None, "Cancel"):
            opcao = 0
        self.close()
        return opcao

    def prompt_new_username(self):
        return super().input_string("Enter new username: ")

    def prompt_new_password(self):
        return super().input_string("Enter your new password:")

    def prompt_new_email(self):
        return super().input_string("Enter new email: ")
