from DAOs.dao import DAO
from models.event.event_attendence import EventAttendence


class EventAttendenceDAO(DAO):
    def __init__(self):
        super().__init__("data/event_attendences.pkl")

    def add(self, event_attendence: EventAttendence):
        if (event_attendence is not None) and isinstance(
            event_attendence, EventAttendence
        ):
            super().add(event_attendence.id, event_attendence)

    def update(self, event_attendence: EventAttendence):
        if (event_attendence is not None) and isinstance(
            event_attendence, EventAttendence
        ):
            super().update(event_attendence.id, event_attendence)

    def get(self, id: int):
        if isinstance(id, int):
            return super().get(id)

    def remove(self, id: int):
        if isinstance(id, int):
            return super().remove(id)
