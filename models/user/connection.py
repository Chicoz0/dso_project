from models.user.connection_status import ConnectionStatus
from models.user.user import User
from DAOs.ids_dao import UniversalID

from exceptions.connection_exceptions import (
    UserNotInConnectionException,
    InvalidConnectionUsersException,
)


class Connection:
    def __init__(
        self,
        user1: User,
        user2: User,
        status: ConnectionStatus = ConnectionStatus.PENDING,
    ):
        if (
            not isinstance(user1, User)
            or not isinstance(user2, User)
            or user1 is None
            or user2 is None
        ):
            raise InvalidConnectionUsersException
        self.__user1 = user1
        self.__user2 = user2
        self.__status = status
        self.__id = UniversalID().get_id()

    @property
    def user1(self):
        return self.__user1

    @property
    def user2(self):
        return self.__user2

    @property
    def status(self):
        return self.__status

    @property
    def id(self):
        return self.__id

    def accept_request(self, user: User):
        if user not in [self.__user1, self.__user2]:
            raise UserNotInConnectionException
        self.__status = ConnectionStatus.ACCEPTED

    def decline_request(self, user: User):
        if user not in [self.__user1, self.__user2]:
            raise UserNotInConnectionException
        self.__status = ConnectionStatus.REJECTED
