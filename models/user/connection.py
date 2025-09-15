from connection_status import ConnectionStatus
from user import User

class Connection:
    def __init__(self, user1: User, user2: User, status: ConnectionStatus = ConnectionStatus.PENDING):
        if not isinstance(user1, User) or not isinstance(user2, User):
            raise TypeError("user1 and user2 must be instances of the User class.")
        self.__user1 = user1
        self.__user2 = user2
        self.__status = status
        self.__strikes = 3

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
    def strikes(self):
        return self.__strikes

    def accept_request(self, user: User):
        if user not in [self.__user1, self.__user2]:
            raise ValueError("Only a user in the connection can accept the request.")   
        self.__status = ConnectionStatus.ACCEPTED
        print(f"Connection between {self.__user1.login} and {self.__user2.login} accepted.")

    def decline_request(self, user: User):
        if user not in [self.__user1, self.__user2]:
            raise ValueError("Only a user in the connection can decline the request.")
        self.__status = ConnectionStatus.REJECTED
        self.__strikes -= 1
        print(f"Connection between {self.__user1.login} and {self.__user2.login} rejected. Trys left: {self.__strikes}.")