import FreeSimpleGUI as sg
from generic_view import GenericView


class ConnectionView(GenericView):
    def show_connection_details(self, connection_data: dict):
        details_text = (
            f"Connection ID: {connection_data['id']}\n"
            f"Status: {connection_data['status']}\n"
            f"Users involved: {connection_data['user1_name']} and {connection_data['user2_name']}"
        )

        layout = [
            [self.header("----- Connection Details -----")],
            [self.title(details_text)],
            [self.title("What do you want to do?")],
            [self.button_key("Dismiss Connection", key="1"), self.button_key("Return to Menu", key="0")]
        ]

        self.window = sg.Window("Connection Details").Layout(layout)

        button, _ = self.read_window()
        self.close()

        if button in (None, "0"):
            return "0"

        return "1"
