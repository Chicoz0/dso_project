from typing import Optional
from datetime import datetime, timedelta
from models.event.attraction import Attraction
from models.event.event import Event
from models.event.event_attendence import EventAttendence
from models.event.age_rating import AgeRating
from models.event.tag import Tag
from models.location.location import Location
from models.user.user import User
from views.event_view import EventView

from controllers.tag_controller import TagController


class EventController:
    def __init__(self, main_controller):
        self.__events = self.__mock_events()
        self.__locations = []
        self.__event_attendances = []
        self.__event_view = EventView()
        self.__main_controller = main_controller
        self.__tag_controller = TagController()

    def __mock_events(self):
        event1 = Event(
            "Event 1",
            User("user 1", "", ""),
            datetime.now() + timedelta(days=1),
            "Event 1 desc",
            AgeRating(1),
            Location("PIDA", "rua lauro", "450A", "Trindade", "Floripa", "0-009"),
        )

        event2 = Event(
            "Event 2",
            User("user 1", "", ""),
            datetime.now(),
            "Event 2 desc",
            AgeRating(3),
            Location("PIDA", "rua lauro", "450A", "Trindade", "Floripa", "0-009"),
        )

        event3 = Event(
            "Event 3",
            User("user 2", "", ""),
            datetime.now(),
            "Event 3 desc",
            AgeRating(2),
            Location("PIDA", "rua lauro", "450A", "Trindade", "Floripa", "0-009"),
        )

        event3.add_tag(Tag("test"))
        event3.add_tag(Tag("Trying"))

        return [event1, event2, event3]

    @property
    def events(self):
        return self.__events

    @property
    def locations(self):
        return self.__locations

    @property
    def event_attendences(self):
        return self.__event_attendances

    def __find_event_by_id(self, id: int):
        for event in self.events:
            if event.id == id:
                return event
        return None

    def __find_event_attendence_by_user_event(self, user: User, event: Event):
        for attendance in self.event_attendences:
            if attendance.user == user and attendance.event == event:
                return attendance
        return None

    def __find_events_user_is_attending(self):
        events = []
        for attendance in self.event_attendences:
            if attendance.user == self.__main_controller.logged_user:
                events.append(attendance.event)
        return events

    def show_event_view(self):
        while True:
            choice = self.__event_view.show_events_menu()

            if choice == 0:
                return
            elif choice == 1:
                self.__list_events()
            elif choice == 2:
                self.__create_event()
            elif choice == 3:
                self.__list_events(self.__main_controller.logged_user)
            elif choice == 4:
                self.__events_user_attending()
            elif choice == 5:
                self.__confirm_attendance()
            elif choice == 6:
                self.__edit_event()

            elif choice == 7:
                self.__delete_event()
            elif choice == 8:
                self.__list_top_5_events()

    def __edit_event(self):
        # print("6 - Add attraction")
        # print("7 - Remove attraction")
        self.__list_events(self.__main_controller.logged_user)
        event_id = self.__event_view.prompt_user_event_id()

        event = self.__find_event_by_id(event_id)

        if event:
            while True:
                choice = self.__event_view.show_edit_event_menu(event.id)

                if choice == 0:
                    return
                elif choice == 1:
                    new_name = self.__event_view.input_string("\nNew event name: ")
                    self.__edit_event_basic_info(event, name=new_name)
                elif choice == 2:
                    new_description = self.__event_view.input_string(
                        "\nNew event description: "
                    )
                    self.__edit_event_basic_info(event, description=new_description)
                elif choice == 3:
                    new_date = self.__event_view.input_date("\nNew event date: ")
                    self.__edit_event_basic_info(event, date=new_date)
                elif choice == 4:
                    self.__add_tag_to_event(event)
                elif choice == 5:
                    self.__remove_tag_from_event(event)
                elif choice == 6:
                    self.__add_attraction_to_event(event)
        else:
            self.__event_view.show_message(
                f"Event with ID {event_id} not found or not authorized to edit"
            )

    def __list_events(self, created_by: Optional[User] = None):
        self.__event_view.show_message("----- List Events -----")
        for event in self.events:
            if not created_by or event.created_by == created_by:
                self.__event_view.show_event(
                    event.id,
                    event.name,
                    event.created_by.username,
                    event.date,
                    event.description,
                    event.age_rating.name,
                )
                if event.tags:
                    self.__tag_controller.show_tags(event.tags)
                if event.attractions:
                    self.__show_attractions(event)

    def __show_attractions(self, event: Event):
        attractions = [
            {"id": a.id, "name": a.name, "type": a.attraction_type}
            for a in event.attractions
        ]
        self.__event_view.show_attractions_one_line(attractions)

    def __add_attraction_to_event(self, event: Event):
        name, type = self.__event_view.prompt_user_attraction_info()
        attraction = Attraction(name, type)
        event.add_attraction(attraction)
        self.__event_view.show_message(f"Attraction {attraction.name} created!")

    def __remove_attraction_from_event(self, event: Event):
        pass

    def __add_tag_to_event(self, event: Event):
        while True:
            if self.__event_view.propmt_user_yes_or_no("Create tag?"):
                self.__tag_controller.create_tag()

            self.__tag_controller.list_tags()
            tag = self.__tag_controller.select_tag_by_id()
            if tag and tag not in event.tags:
                event.add_tag(tag)
                self.__event_view.show_message(f"Tag {tag.slug} added")
            return

    def __remove_tag_from_event(self, event: Event):
        self.__tag_controller.list_tags(event.tags)
        tag = self.__tag_controller.select_tag_by_id()

        if tag in event.tags:
            event.remove_tag(tag)
            self.__event_view.show_message(f"Tag {tag.slug} removed!")
        else:
            self.__event_view.show_message(f"Tag not in event")

    def __edit_event_basic_info(
        self,
        event: Event,
        name: Optional[str] = None,
        description: Optional[str] = None,
        date: Optional[datetime] = None,
    ):
        if name:
            event.name = name
            self.__event_view.show_message("Name updated")
        elif description:
            event.description = description
            self.__event_view.show_message("Description updated")
        elif date:
            event.date = date
            self.__event_view.show_message("Date updated")

    def __create_event(self):
        name, description, date = self.__event_view.prompt_event_info()

        (
            l_name,
            l_street,
            l_suite,
            l_neighborhood,
            l_city,
            l_zip_code,
        ) = self.__event_view.prompt_event_location_info()

        location = Location(
            l_name, l_street, l_suite, l_neighborhood, l_city, l_zip_code
        )

        for age_rating in AgeRating:
            self.__event_view.show_age_rating(age_rating.name, age_rating.value)

        age_rating_value = self.__event_view.propmt_user_for_age_rating(
            [a.value for a in AgeRating]
        )

        age_rating_event = AgeRating(age_rating_value)

        event = Event(
            name,
            self.__main_controller.logged_user,
            date,
            description,
            age_rating_event,
            location,
        )

        self.events.append(event)
        self.__event_view.show_message(f"Event with ID {event.id} created!")

    def __events_user_attending(self):
        events = self.__find_events_user_is_attending()
        if events:
            self.__event_view.show_message("Events user's attending:")
            for event in events:
                self.__event_view.show_event(
                    event.id,
                    event.name,
                    event.created_by.username,
                    event.date,
                    event.description,
                    event.age_rating.name,
                )
        else:
            self.__event_view.show_message("User isn't attending any events!")

    def __confirm_attendance(self):
        self.__list_events()

        event_id = self.__event_view.prompt_user_event_id()

        self.__event_view.show_message("Select event to confirm attendance")
        event = self.__find_event_by_id(event_id)

        if event:
            if self.__find_event_attendence_by_user_event(
                self.__main_controller.logged_user, event
            ):
                self.__event_view.show_message(
                    f"Already confirmed attendance for event ID {event.id}!"
                )
                return

            attendance = EventAttendence(self.__main_controller.logged_user, event)
            self.event_attendences.append(attendance)
            self.__event_view.show_message(f"Attendance confirmed for event {event.id}")

        else:
            self.__event_view.show_message(f"Event with ID {event_id} not found")

    def __delete_event(self):
        self.__list_events(self.__main_controller.logged_user)

        event_id = self.__event_view.prompt_user_event_id()
        event = self.__find_event_by_id(event_id)

        if event:
            if event.created_by == self.__main_controller.logged_user:
                if self.__event_view.propmt_user_yes_or_no("Are you sure?"):
                    self.events.remove(event)
                    self.__event_view.show_message(f"Event with ID {event.id} deleted")
            else:
                self.__event_view.show_message(
                    f"No permission to delete with with ID {event.id}"
                )
        else:
            self.__event_view.show_message(f"Event with ID {event_id} not found")
    
    # Report
    def __list_top_5_events(self):
        future_events = [event for event in self.events if event.date >= datetime.now()]

        event_attendance_counts = {}
        for event in future_events:
            count = 0
            for attendance in self.event_attendences:
                if attendance.event.id == event.id:
                    count += 1
            event_attendance_counts[event] = count

        sorted_events = sorted(event_attendance_counts.items(), key=lambda item: item[1], reverse=True)
        top_5_events = sorted_events[:5]
        self.__event_view.show_top_5_events_report(top_5_events)

