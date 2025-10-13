from models.user.connection import Connection
from models.user.connection_status import ConnectionStatus
from models.user.user import User
from views.logged_user_view import LoggedUserView

class ConnectionController:
    def __init__(self):
        self.__user_view = LoggedUserView()
        self.__connections = []

    def create_connection(self, user1: User, user2: User) -> Connection:        
        existing_connection = self.get_connection_between_users(user1, user2)
        if existing_connection:
            self.__user_view.show_connection_already_exists()
            return existing_connection

        new_connection = Connection(user1, user2)
        self.__connections.append(new_connection)
        self.__user_view.show_operation_done_message
    
    def get_connection_between_users(self, user1: User, user2: User) -> Connection | None:
        for connection in self.__connections:
            if (connection.user1 == user1 and connection.user2 == user2) or \
               (connection.user1 == user2 and connection.user2 == user1):
                return connection
        return None
