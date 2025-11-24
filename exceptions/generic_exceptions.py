class NotFoundException(Exception):
    def __init__(self, message="Not Found!") -> None:
        super().__init__(self, message)
