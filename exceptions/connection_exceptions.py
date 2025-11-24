class UserNotInConnectionException(Exception):
    def __init__(
        self, message="Only a user in the connection can perform this action."
    ) -> None:
        super().__init__(self, message)


class InvalidConnectionUsersException(Exception):
    def __init__(self, message="Both users need to be valid") -> None:
        super().__init__(self, message)
