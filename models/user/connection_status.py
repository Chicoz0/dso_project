from enum import Enum

class ConnectionStatus(Enum):
    PENDING = 1
    REJECTED = 2
    ACCEPTED = 3