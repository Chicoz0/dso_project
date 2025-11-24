from datetime import datetime
from views.generic_view import GenericView


class EventView(GenericView):
    def show_events_menu(self):
        layout = [
            [sg.Text("----- Events -----", font=("Helvica", 25))],
            [sg.Button("List all events", key="1", size=(25, 1))],
            [sg.Button("Create event", key="2", size=(25, 1))],
            [sg.Button("My events", key="3", size=(25, 1))],
            [sg.Button("Events I'm attending", key="4", size=(25, 1))],
            [sg.Button("Confirm attendance", key="5", size=(25, 1))],
            [sg.Button("Edit event", key="6", size=(25, 1))],
            [sg.Button("Delete event", key="7", size=(25, 1))],
            [sg.Button("Top 5 events (Report)", key="8", size=(25, 1))],
            [sg.Button("Back", key="0", size=(25, 1), button_color=('white', 'firebrick3'))]
        ]
        self.window = sg.Window("EventLink - Events").Layout(layout)

        button, _ = self.read_window()
        self.close()

        if button in (None, "Back"):
            return 0
        return int(button)

    def show_event(
        self,
        event_id: int,
        event_name: str,
        event_creator: str,
        event_date: datetime,
        event_description: str,
        age_rating: str,
    ):
        msg = (
            f"ID: {event_id}\n"
            f"Name: {event_name}\n"
            f"Created By: {event_creator}\n"
            f"Date: {event_date.date()}\n"
            f"Description: {event_description}\n"
            f"Rating: {age_rating}"
        )
        sg.popup_scrolled(msg, title=f"Event Details: {event_name}", size=(50, 10))

    def show_attractions_one_line(self, attractions: list):
        msg = "Attractions List:\n\n"
        for attraction in attractions:
            msg += f"ID: {attraction.get('id')}, Name: {attraction.get('name')}, Type: {attraction.get('type')}\n"
 
        sg.popup_scrolled(msg, title="Attractions")

    def show_edit_event_menu(self, event_id: int):
        layout = [
            [sg.Text(f"----- Edit Event {event_id} -----", font=("Helvica", 20))],
            [sg.Button("Edit name", key="1", size=(20, 1))],
            [sg.Button("Edit description", key="2", size=(20, 1))],
            [sg.Button("Edit date", key="3", size=(20, 1))],
            [sg.Button("Add tag", key="4", size=(20, 1))],
            [sg.Button("Remove tag", key="5", size=(20, 1))],
            [sg.Button("Add attraction", key="6", size=(20, 1))],
            [sg.Button("Back", key="0", size=(20, 1))]
        ]
        self.window = sg.Window("Edit Menu").Layout(layout)

        button, _ = self.read_window()
        self.close()

        if button in (None, "Back"):
            return 0
        return int(button)

    def show_age_rating(self, name, value):
        super().show_message(f"{value} - {name}")

    # Report
    def show_top_5_events_report(self, events_with_counts: list):
        if not events_with_counts:
            super().show_message("No future events found with confirmations.")
            return
 
        msg = "----- Top 5 Next Events with most confirmations -----\n\n"
        for i, (event, count) in enumerate(events_with_counts):
            msg += (
                f"#{i+1}:\n"
                f"ID: {event.id} | Name: {event.name}\n"
                f"Created By: {event.created_by.username}\n"
                f"Confirmations: {count}\n"
                f"-----------------------------\n"
            )
        sg.popup_scrolled(msg, title="Top 5 Report", size=(50, 15))

    def propmt_user_for_age_rating(self, valid_values):
        return super().input_specific_int("Select an age rating for the Event: ", valid_values)

    def prompt_user_attraction_info(self):
        layout = [
            [sg.Text("Create Attraction", font=("Helvica", 15))],
            [sg.Text("Name:"), sg.InputText(key="name")],
            [sg.Text("Type:"), sg.InputText(key="type")],
            [sg.Button("Confirm"), sg.Cancel()]
        ]
        self.window = sg.Window("New Attraction").Layout(layout)
        button, values = self.read_window()
        self.close()

        if button in (None, "Cancel"):
            return None, None
        return values["name"], values["type"]

    def prompt_event_info(self):
        layout = [
            [sg.Text("Create Event", font=("Helvica", 15))],
            [sg.Text("Name:"), sg.InputText(key="name")],
            [sg.Text("Description:"), sg.InputText(key="desc")],
            [sg.Text("Date (DD/MM/YYYY):"), sg.InputText(key="date")],
            [sg.Button("Confirm"), sg.Cancel()]
        ]
        self.window = sg.Window("New Event").Layout(layout)

        while True:
            button, values = self.read_window()
            if button in (None, "Cancel"):
                self.close()
                return None, None, None
            
            try:
                date_obj = datetime.strptime(values["date"], "%d/%m/%Y")
                self.close()
                return values["name"], values["desc"], date_obj
            except ValueError:
                sg.popup("Invalid Date format! Use DD/MM/YYYY")

    def prompt_event_location_info(self):
        layout = [
            [sg.Text("Event Location", font=("Helvica", 15))],
            [sg.Text("Location Name:"), sg.InputText(key="loc_name")],
            [sg.Text("Street Name:"), sg.InputText(key="street")],
            [sg.Text("Suite/Number:"), sg.InputText(key="suite")],
            [sg.Text("Neighborhood:"), sg.InputText(key="neighborhood")],
            [sg.Text("City:"), sg.InputText(key="city")],
            [sg.Text("Zip Code:"), sg.InputText(key="zip")],
            [sg.Button("Confirm"), sg.Cancel()]
        ]
        self.window = sg.Window("Location Info").Layout(layout)
        
        button, values = self.read_window()
        self.close()

        if button in (None, "Cancel"):
            return "", "", "", "", "", ""

        return (
            values["loc_name"], values["street"], values["suite"],
            values["neighborhood"], values["city"], values["zip"]
        )

    def prompt_user_event_id(self):
        return super().input_int("Select event ID: ")
