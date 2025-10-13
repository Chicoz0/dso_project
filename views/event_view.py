from datetime import datetime
from views.generic_view import GenericView


class EventView(GenericView):
    def show_events_menu(self):
        print(f"\n----- Events -----")
        print("1 - List all events")
        print("2 - Create event")
        print("3 - My events")
        print("4 - Events I'm attending")
        print("5 - Confirm attendance")
        print("6 - Edit event")
        print("7 - Delete event")
        print("8 - Top 5 events with most confirmations")
        print("0 - back")
        choice = self.input_int("Choose an option: ")
        return choice

    def show_event(
        self,
        event_id: int,
        event_name: str,
        event_creator: str,
        event_date: datetime,
        event_description: str,
        age_rating: str,
    ):
        print(f"\nID: {event_id}")
        print(f"Name: {event_name}")
        print(f"Created By: {event_creator}")
        print(f"Date: {event_date.date()}")
        print(f"Description: {event_description}")
        print(f"Rating: {age_rating}")

    def show_attractions_one_line(self, attractions: list):
        print("Attractions: ", end="")
        for attraction in attractions:
            id = attraction.get("id")
            name = attraction.get("name")
            type = attraction.get("type")
            print(f"ID: {id}, name: {name}, type: {type} -", end="")

    def show_edit_event_menu(self, event_id: int):
        print(f"----- Edit Event {event_id} -----")
        print("1 - Edit name")
        print("2 - Edit description")
        print("3 - Edit date")
        print("4 - Add tag")
        print("5 - Remove tag")
        print("6 - Add attraction")
        print("0 - back")

        choice = super().input_int("Choose: ")
        return choice

    def show_age_rating(self, name, value):
        print(f"{value} - {name} ")
    
    # Report
    def show_top_5_events_report(self, events_with_counts: list):
        print("\n----- Top 5 Next Events with most confirmations -----")
        if not events_with_counts:
            print("No future events found with confirmations.")
            return
            
        for i, (event, count) in enumerate(events_with_counts):
            print(f"\n#{i+1}:")
            print(f"ID: {event.id}")
            print(f"Name: {event.name}")
            print(f"Created By: {event.created_by.username}")
            print(f"Confirmations: {count}")

    def propmt_user_for_age_rating(self, valid_values):
        age_rating_value = super().input_specific_int(
            "Select an age rating for the Event: ", valid_values
        )
        return age_rating_value

    def prompt_user_attraction_info(self):
        print("\n----- Create Attraction -----")
        name = super().input_string("Attraction name: ")
        type = super().input_string("Attriaction type: ")

        return name, type

    def prompt_event_info(self):
        print(f"\n ----- Event Creation -----")
        name = super().input_string("Insert event name: ")
        description = super().input_string("Insert event description: ")
        date = super().input_date("Insert event date (DD/MM/YYYY): ")

        return name, description, date

    def prompt_event_location_info(self):
        print("\nWhere will the event happen?")
        location_name = super().input_string("Location name: ")
        location_street = super().input_string("Street name: ")
        location_suite = super().input_string("Suite number: ")
        location_neighborhood = super().input_string("Neighborhood: ")
        location_city = super().input_string("City: ")
        location_zip_code = super().input_string("Zip Code: ")

        return (
            location_name,
            location_street,
            location_suite,
            location_neighborhood,
            location_city,
            location_zip_code,
        )

    def prompt_user_event_id(self):
        return super().input_int("\nSelect event ID: ")
