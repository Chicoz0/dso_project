from connection_status import ConnectionStatus
from user import User
from utils.id import generate_id

class Connection:
    def __init__(self, user1: User, user2: User, status: ConnectionStatus = ConnectionStatus.PENDING):
        if not isinstance(user1, User) or not isinstance(user2, User) or user1 is None or user2 is None:
            raise TypeError("Both users must be instances of the User class and not None.")
        self.__user1 = user1
        self.__user2 = user2
        self.__status = status
        self.__id = generate_id()

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
            raise ValueError("Only a user in the connection can accept the request.")   
        self.__status = ConnectionStatus.ACCEPTED
        print(f"Connection between {self.__user1.login} and {self.__user2.login} accepted.")

    def decline_request(self, user: User):
        if user not in [self.__user1, self.__user2]:
            raise ValueError("Only a user in the connection can decline the request.")
        self.__status = ConnectionStatus.REJECTED
        print(f"Connection between {self.__user1.login} and {self.__user2.login} rejected.")