from DAOs.dao import DAO
from models.event.event import Event


class EventDAO(DAO):
    def __init__(self):
        super().__init__("data/events.pkl")

    def add(self, event: Event):
        if (event is not None) and isinstance(event, Event):
            super().add(event.id, event)

    def update(self, event: Event):
        if (event is not None) and isinstance(event, Event):
            super().update(event.id, event)

    def get(self, id: int):
        if isinstance(id, int):
            return super().get(id)

    def remove(self, id: int):
        if isinstance(id, int):
            return super().remove(id)
