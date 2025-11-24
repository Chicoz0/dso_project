from datetime import datetime
from views.generic_view import GenericView

import FreeSimpleGUI as sg


class EventView(GenericView):
    def show_events_menu(self):
        layout = [
            [self.header("----- Events -----")],
            [self.button_key("List all events", key="1")],
            [self.button_key("Create event", key="2")],
            [self.button_key("My events", key="3")],
            [self.button_key("Events I'm attending", key="4")],
            [self.button_key("Confirm attendance", key="5")],
            [self.button_key("Edit event", key="6")],
            [self.button_key("Delete event", key="7")],
            [self.button_key("Top 5 events (Report)", key="8")],
            [self.button_key("Back", key="0")],
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
        self.popup_scrolled(msg, title=f"Event Details: {event_name}")

    def show_events(self, events):
        if events:
            msg = []
            for e in events:
                event_id = e.get("event_id")
                even_name = e.get("event_name")
                event_creator = e.get("event_creator")
                event_date = e.get("event_date")
                event_description = e.get("event_description")
                age_rating = e.get("age_rating")
                tags_msg = ""

                for t in e.get("event_tags"):
                    name = t.get("tag_name")
                    m = f"Tag Name: {name}"
                    tags_msg += m

                msg.append(
                    f"ID: {event_id}\nName: {even_name}\nCreated By: {event_creator}\nDate: {event_date}\nDescription: {event_description}\nRating: {age_rating}\nTags:\n{tags_msg}"
                )

            str_msg = "\n\n".join(msg)
            self.popup_scrolled(str_msg, title="Event Details")
        else:
            self.popup("No events found!")

    def show_attractions_one_line(self, attractions: list):
        msg = "Attractions List:\n\n"
        for attraction in attractions:
            msg += f"ID: {attraction.get('id')}, Name: {attraction.get('name')}, Type: {attraction.get('type')}\n"

        self.popup_scrolled(msg, title="Attractions")

    def show_edit_event_menu(self, event_id: int):
        layout = [
            [self.header(f"----- Edit Event {event_id} -----")],
            [self.button_key("Edit name", key="1")],
            [self.button_key("Edit description", key="2")],
            [self.button_key("Edit date", key="3")],
            [self.button_key("Add tag", key="4")],
            [self.button_key("Remove tag", key="5")],
            [self.button_key("Add attraction", key="6")],
            [self.button_key("Back", key="0")],
        ]
        self.window = sg.Window("Edit Menu").Layout(layout)

        button, _ = self.read_window()
        self.close()

        if button in (None, "Back"):
            return 0
        return int(button)

    def show_age_ratings(self, ratings):
        msg = []
        for r in ratings:
            value = r.get("value")
            name = r.get("name")
            s = f"{value} - {name}"
            msg.append(s)
        m = "\n".join(msg)
        super().show_message(m)

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
        self.popup_scrolled(msg, title="Top 5 Report")

    def propmt_user_for_age_rating(self, valid_values):
        return super().input_specific_int(
            "Select an age rating for the Event: ", valid_values
        )

    def prompt_user_attraction_info(self):
        layout = [
            [self.header("Create Attraction")],
            [self.input_title("Name:"), self.input_text(key="name")],
            [self.input_title("Type:"), self.input_text(key="type")],
            [self.confirm(), self.cancel()],
        ]
        self.window = sg.Window("New Attraction").Layout(layout)
        button, values = self.read_window()
        self.close()

        if button in (None, "Cancel"):
            return None, None
        return values["name"], values["type"]

    def prompt_event_info(self):
        layout = [
            [self.header("Create Event")],
            [self.input_title("Name:"), self.input_text(key="name")],
            [self.input_title("Description:"), self.input_text(key="desc")],
            [self.input_title("Date (DD/MM/YYYY):"), self.input_text(key="date")],
            [self.confirm()],
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
                self.popup("Invalid Date format! Use DD/MM/YYYY")

    def prompt_event_location_info(self):
        layout = [
            [self.header("Event Location")],
            [self.input_title("Location Name:"), self.input_text(key="loc_name")],
            [self.input_title("Street Name:"), self.input_text(key="street")],
            [self.input_title("Suite/Number:"), self.input_text(key="suite")],
            [self.input_title("Neighborhood:"), self.input_text(key="neighborhood")],
            [self.input_title("City:"), self.input_text(key="city")],
            [self.input_title("Zip Code:"), self.input_text(key="zip")],
            [self.confirm()],
        ]
        self.window = sg.Window("Location Info").Layout(layout)

        button, values = self.read_window()
        self.close()

        if button in (None, "Cancel"):
            return "", "", "", "", "", ""

        return (
            values["loc_name"],
            values["street"],
            values["suite"],
            values["neighborhood"],
            values["city"],
            values["zip"],
        )

    def prompt_user_event_id(self):
        return super().input_int("Select event ID: ")
