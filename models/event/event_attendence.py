from models.user.user import User
from models.event.event import Event

from DAOs.ids_dao import UniversalID


class EventAttendence:
    def __init__(self, user: User, event: Event):
        if not isinstance(user, User):
            raise Exception("Invalid user")

        if not isinstance(event, Event):
            raise Exception("Invalid event")

        self.__id = UniversalID().get_id()
        self.__user = user
        self.__event = event

    @property
    def id(self):
        return self.__id

    @property
    def user(self):
        return self.__user

    @property
    def event(self):
        return self.__event
