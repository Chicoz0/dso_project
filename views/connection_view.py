from generic_view import GenericView


class ConnectionView(GenericView):
    def show_connection_details(self, connection_data: dict):
        details_text = (
            f"Connection ID: {connection_data['id']}\n"
            f"Status: {connection_data['status']}\n"
            f"Users involved: {connection_data['user1_name']} and {connection_data['user2_name']}"
        )

        layout = [
            [sg.Text("----- Connection Details -----", font=("Helvica", 20))],
            [sg.Text(details_text, font=("Helvica", 12))],
            [sg.Text("What do you want to do?", pad=(0, 20))],
            [sg.Button("Dismiss Connection", key="1"), sg.Button("Return to Menu", key="0")]
        ]

        self.window = sg.Window("Connection Details").Layout(layout)

        button, _ = self.read_window()
        self.close()

        if button in (None, "0"):
            return "0"

        return "1"
