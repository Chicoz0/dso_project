from DAOs.dao import DAO
from models.user.connection import Connection

class ConnectionDAO(DAO):
    def __init__(self):
        super().__init__('data/connections.pkl')

    def add(self, connection: Connection):
        if((connection is not None) and isinstance(connection, Connection) and isinstance(connection.id, int)):
            super().add(connection.id, connection)

    def update(self, connection: Connection):
        if((connection is not None) and isinstance(connection, Connection) and isinstance(connection.id, int)):
            super().update(connection.id, connection)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, int)):
            return super().remove(key)
