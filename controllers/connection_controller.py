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
    
    def accept_connection(self, connection_id: int, user: User) -> Connection | None:
        connection = self.find_connection_by_id(connection_id)
        if not connection:
            self.__user_view.show_connection_not_found(connection_id)
            return self.__user_view.show_pending_connection_requests()# Colocar aqui a referencia de user
        #logica n finalizada, vou ajustar 
    
    def get_connection_between_users(self, user1: User, user2: User) -> Connection | None:
        for connection in self.__connections:
            if (connection.user1 == user1 and connection.user2 == user2) or \
               (connection.user1 == user2 and connection.user2 == user1):
                return connection
        return None
    
    def find_connection_by_id(self, connection_id: int) -> Connection | None:
        for connection in self.__connections:
            if connection.id == connection_id:
                return connection
        return None
    
    def get_user_connections(self, user: User) -> list[Connection]:
        user_connections = []
        for connection in self.__connections:
            if user in [connection.user1, connection.user2]:
                user_connections.append(connection)
        return user_connections
